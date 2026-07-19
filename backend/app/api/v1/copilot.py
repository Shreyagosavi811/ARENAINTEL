from fastapi import APIRouter, Depends
from typing import Tuple
from ...application.copilot.schemas import AnalyzeSituationRequest, AnalyzeSituationResponse
from ...application.copilot.analyze_situation import CopilotUseCase
from ...application.copilot.prompt_builder import PromptBuilder
from ..dependencies.auth import get_current_user_and_role
from ..dependencies.core import get_ai_provider, get_retriever, get_context_service
from ...infrastructure.ai.provider import IAIProvider
from ...infrastructure.retrieval.provider import IRetriever
from ...application.copilot.context_service import ContextService

router = APIRouter()

def get_copilot_use_case(
    ai: IAIProvider = Depends(get_ai_provider),
    retriever: IRetriever = Depends(get_retriever),
    context_service: ContextService = Depends(get_context_service)
) -> CopilotUseCase:
    return CopilotUseCase(
        ai_provider=ai,
        retriever=retriever,
        context_service=context_service,
        prompt_builder=PromptBuilder()
    )

@router.post("/analyze", response_model=AnalyzeSituationResponse)
async def analyze_situation(
    request: AnalyzeSituationRequest, 
    identity: Tuple[str, str] = Depends(get_current_user_and_role),
    use_case: CopilotUseCase = Depends(get_copilot_use_case)
):
    _, role = identity
    return await use_case.execute(request, user_role=role)
