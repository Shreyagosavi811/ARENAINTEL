from fastapi import APIRouter, Depends
from typing import Tuple
from ...application.incidents.schemas import ReportIncidentRequest, ReportIncidentResponse
from ...application.incidents.report_incident import ReportIncidentUseCase
from ...application.incidents.prompt_builder import IncidentPromptBuilder
from ..dependencies.auth import get_current_user_and_role
from ..dependencies.core import get_ai_provider, get_retriever, get_audit_logger
from ...infrastructure.ai.provider import IAIProvider
from ...infrastructure.retrieval.provider import IRetriever
from ...infrastructure.audit.logger import AuditLogger

router = APIRouter()

def get_incident_use_case(
    ai: IAIProvider = Depends(get_ai_provider),
    retriever: IRetriever = Depends(get_retriever),
    audit_logger: AuditLogger = Depends(get_audit_logger)
) -> ReportIncidentUseCase:
    return ReportIncidentUseCase(
        ai_provider=ai,
        retriever=retriever,
        prompt_builder=IncidentPromptBuilder(),
        audit_logger=audit_logger
    )

@router.post("/report", response_model=ReportIncidentResponse)
async def report_incident(
    request: ReportIncidentRequest, 
    identity: Tuple[str, str] = Depends(get_current_user_and_role),
    use_case: ReportIncidentUseCase = Depends(get_incident_use_case)
):
    user_id, _ = identity
    return await use_case.execute(request, actor_id=user_id)
