from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from typing import Tuple
from ...application.approvals.schemas import ProcessApprovalRequest, ProcessApprovalResponse
from ...application.approvals.process_approval import ProcessApprovalUseCase
from ..dependencies.auth import get_current_user_and_role
from ..dependencies.core import get_recommendation_repository, get_audit_logger
from ...infrastructure.persistence.repository import IRecommendationRepository
from ...infrastructure.audit.logger import AuditLogger

router = APIRouter()

def get_approval_use_case(
    repo: IRecommendationRepository = Depends(get_recommendation_repository),
    audit_logger: AuditLogger = Depends(get_audit_logger)
) -> ProcessApprovalUseCase:
    return ProcessApprovalUseCase(repository=repo, audit_logger=audit_logger)

@router.post("/{recommendation_id}/approve", response_model=ProcessApprovalResponse)
async def process_approval(
    recommendation_id: UUID,
    request: ProcessApprovalRequest,
    identity: Tuple[str, str] = Depends(get_current_user_and_role),
    use_case: ProcessApprovalUseCase = Depends(get_approval_use_case)
):
    user_id, role = identity
    return await use_case.execute(recommendation_id, request, user_id=user_id, role=role)
