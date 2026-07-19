from .schemas import AnalyzeSituationRequest, AnalyzeSituationResponse, ActionCapabilities, CopilotAIResponse, MatchdayContext
from .context_service import ContextService
from .prompt_builder import PromptBuilder
from ...infrastructure.ai.provider import IAIProvider
from ...infrastructure.retrieval.provider import IRetriever
from ...infrastructure.caching.analysis_cache import analysis_cache
import time
import logging

logger = logging.getLogger("stadiumops.copilot")

class CopilotUseCase:
    def __init__(self, ai_provider: IAIProvider, retriever: IRetriever, context_service: ContextService, prompt_builder: PromptBuilder):
        self.ai_provider = ai_provider
        self.retriever = retriever
        self.context_service = context_service
        self.prompt_builder = prompt_builder
    
    async def execute(self, request: AnalyzeSituationRequest, user_role: str) -> AnalyzeSituationResponse:
        # Default matchday context if none provided by client
        matchday_ctx = request.matchday_context or MatchdayContext()
        ctx_dict = matchday_ctx.model_dump()
        
        # 1. Check Cache
        cached_data = analysis_cache.get(request.text, ctx_dict)
        if cached_data:
            logger.info("Cache Hit - Returning cached operational analysis")
            cached_data["capabilities"] = ActionCapabilities(
                can_approve=(user_role in ["supervisor", "admin"]),
                can_execute=False
            )
            return AnalyzeSituationResponse.model_validate(cached_data)

        logger.info("Cache Miss - Processing new operational analysis")
        
        t0 = time.time()
        # 2. Collect Context
        live_context = await self.context_service.get_current_context()
        
        # 3. Retrieve Knowledge
        docs = await self.retriever.retrieve(request.text, top_k=2)
        source_ids = [d.id for d in docs]
        
        # Calculate retrieval confidence (simple metric based on chunks found)
        confidence_level = "High" if len(docs) >= 2 else "Medium" if len(docs) == 1 else "Low"
        retrieval_confidence = f"{confidence_level} ({len(docs)} relevant SOP sections found)"
        
        rag_latency = (time.time() - t0) * 1000
        logger.info(f"RAG Retrieval Latency: {rag_latency:.2f}ms")
        
        # 4. Build Prompt with Matchday Context
        t1 = time.time()
        prompt = self.prompt_builder.build_analysis_prompt(request.text, live_context, docs, matchday_ctx)
        
        # 5. Ask GenAI
        ai_response = await self.ai_provider.generate_structured_output(prompt, CopilotAIResponse)
        ai_latency = (time.time() - t1) * 1000
        logger.info(f"GenAI Inference Latency: {ai_latency:.2f}ms")
        
        # 6. Prepare Response
        capabilities = ActionCapabilities(
            can_approve=(user_role in ["supervisor", "admin"]),
            can_execute=False
        )
        
        response_obj = AnalyzeSituationResponse(
            summary=ai_response.summary,
            risk_level=ai_response.risk_level,
            risks=ai_response.risks,
            recommendations=ai_response.recommendations,
            uncertainties=ai_response.uncertainties,
            sources=source_ids,
            retrieval_confidence=retrieval_confidence,
            impact_estimate=ai_response.impact_estimate,
            capabilities=capabilities
        )
        
        # Cache the result (exclude dynamic capabilities which depend on user role)
        cacheable_data = response_obj.model_dump(mode="json")
        del cacheable_data["capabilities"]
        analysis_cache.set(request.text, ctx_dict, cacheable_data)
        
        return response_obj
