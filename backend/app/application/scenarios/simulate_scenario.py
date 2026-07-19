import copy
from .schemas import SimulateScenarioRequest, ScenarioSimulationResponse, ScenarioSimulationAIResponse
from .prompt_builder import ScenarioPromptBuilder
from ..copilot.context_service import ContextService
from ...infrastructure.ai.provider import IAIProvider
from ...infrastructure.retrieval.provider import IRetriever

class SimulateScenarioUseCase:
    def __init__(self, ai_provider: IAIProvider, retriever: IRetriever, context_service: ContextService, prompt_builder: ScenarioPromptBuilder):
        self.ai_provider = ai_provider
        self.retriever = retriever
        self.context_service = context_service
        self.prompt_builder = prompt_builder
    
    async def execute(self, request: SimulateScenarioRequest) -> ScenarioSimulationResponse:
        # 1. Fetch CURRENT state
        real_context = await self.context_service.get_current_context()
        
        # 2. Create HYPOTHETICAL state
        # A deepcopy ensures that no modifications can accidentally leak into the real_context object in memory
        hypothetical_context = copy.deepcopy(real_context)
        
        # (In a more advanced implementation, the AI or a parser might proactively mutate hypothetical_context 
        # based on the query before analysis, e.g., closing a gate. For now, the deepcopy serves as the distinct boundary).
        
        # 3. Retrieve Knowledge
        docs = await self.retriever.retrieve(request.what_if_query, top_k=2)
        source_ids = [d.id for d in docs]
        
        # 4. Build Prompt strictly using hypothetical_context
        prompt = self.prompt_builder.build_simulation_prompt(request.what_if_query, hypothetical_context, docs)
        
        # 5. Ask GenAI
        ai_response = await self.ai_provider.generate_structured_output(prompt, ScenarioSimulationAIResponse)
        
        return ScenarioSimulationResponse(
            scenario_query=request.what_if_query,
            is_hypothetical_simulation=True, # Explicit hardcoded flag for safety
            expected_impacts=ai_response.expected_impacts,
            potential_risks=ai_response.potential_risks,
            mitigations=ai_response.mitigations,
            affected_stakeholders=ai_response.affected_stakeholders,
            communication_requirements=ai_response.communication_requirements,
            assumptions=ai_response.assumptions,
            uncertainty=ai_response.uncertainty,
            sources=source_ids
        )
