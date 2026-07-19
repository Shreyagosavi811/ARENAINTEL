from fastapi import APIRouter, Depends
from ...application.scenarios.schemas import SimulateScenarioRequest, ScenarioSimulationResponse
from ...application.scenarios.simulate_scenario import SimulateScenarioUseCase
from ...application.scenarios.prompt_builder import ScenarioPromptBuilder
from ..dependencies.core import get_ai_provider, get_retriever, get_context_service
from ...infrastructure.ai.provider import IAIProvider
from ...infrastructure.retrieval.provider import IRetriever
from ...application.copilot.context_service import ContextService

router = APIRouter()

def get_scenario_use_case(
    ai: IAIProvider = Depends(get_ai_provider),
    retriever: IRetriever = Depends(get_retriever),
    context_service: ContextService = Depends(get_context_service)
) -> SimulateScenarioUseCase:
    return SimulateScenarioUseCase(
        ai_provider=ai,
        retriever=retriever,
        context_service=context_service,
        prompt_builder=ScenarioPromptBuilder()
    )

@router.post("/simulate", response_model=ScenarioSimulationResponse)
async def simulate_scenario(
    request: SimulateScenarioRequest, 
    use_case: SimulateScenarioUseCase = Depends(get_scenario_use_case)
):
    return await use_case.execute(request)
