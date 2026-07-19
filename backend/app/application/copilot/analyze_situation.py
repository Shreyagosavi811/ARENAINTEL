from .schemas import AnalyzeSituationRequest, AnalyzeSituationResponse, ActionCapabilities, CopilotAIResponse
from .context_service import ContextService
from .prompt_builder import PromptBuilder
from ...infrastructure.ai.provider import IAIProvider
from ...infrastructure.retrieval.provider import IRetriever

class CopilotUseCase:
    def __init__(self, ai_provider: IAIProvider, retriever: IRetriever, context_service: ContextService, prompt_builder: PromptBuilder):
        self.ai_provider = ai_provider
        self.retriever = retriever
        self.context_service = context_service
        self.prompt_builder = prompt_builder
    
    async def execute(self, request: AnalyzeSituationRequest, user_role: str) -> AnalyzeSituationResponse:
        # 1. Collect Context
        live_context = await self.context_service.get_current_context()
        
        # 2. Retrieve Knowledge
        docs = await self.retriever.retrieve(request.text, top_k=2)
        source_ids = [d.id for d in docs]
        
        # 3. Build Prompt
        prompt = self.prompt_builder.build_analysis_prompt(request.text, live_context, docs)
        
        # 4. Ask GenAI
        ai_response = await self.ai_provider.generate_structured_output(prompt, CopilotAIResponse)
        
        # 5. UI Capabilities
        capabilities = ActionCapabilities(
            can_approve=(user_role in ["supervisor", "admin"]),
            can_execute=False
        )
        
        return AnalyzeSituationResponse(
            summary=ai_response.summary,
            risk_level=ai_response.risk_level,
            risks=ai_response.risks,
            recommendations=ai_response.recommendations,
            uncertainties=ai_response.uncertainties,
            sources=source_ids,
            capabilities=capabilities
        )
