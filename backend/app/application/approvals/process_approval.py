from uuid import UUID
from fastapi import HTTPException
from .schemas import ProcessApprovalRequest, ProcessApprovalResponse
from ...domain.enums.ai import ApprovalDecisionType, RecommendationStatus
from ...domain.models.audit import ApprovalDecision
from ...domain.rules.state_machine import transition_recommendation, InvalidStateTransitionError
from ...infrastructure.persistence.repository import IRecommendationRepository
from ...infrastructure.audit.logger import AuditLogger

class ProcessApprovalUseCase:
    def __init__(self, repository: IRecommendationRepository, audit_logger: AuditLogger):
        self.repository = repository
        self.audit_logger = audit_logger
        
    async def execute(self, recommendation_id: UUID, request: ProcessApprovalRequest, user_id: str, role: str) -> ProcessApprovalResponse:
        # 1. Authentication Check (Explicit enforcement)
        if not user_id or not role:
            raise HTTPException(status_code=401, detail="Unauthenticated user cannot approve.")
            
        # 2. Authorization Check (Only supervisor or admin can approve)
        if role not in ["supervisor", "admin"]:
            raise HTTPException(status_code=403, detail="Unauthorized user cannot approve recommendations.")
            
        # 3. Retrieve Recommendation
        recommendation = await self.repository.get(recommendation_id)
        if not recommendation:
            raise HTTPException(status_code=404, detail="Recommendation not found.")
            
        # 4. Determine target state
        target_status = RecommendationStatus.APPROVED if request.decision == ApprovalDecisionType.APPROVE else RecommendationStatus.REJECTED
        
        # 5. State Machine Validation
        try:
            new_status = transition_recommendation(recommendation.status, target_status)
        except InvalidStateTransitionError as e:
            raise HTTPException(status_code=400, detail=str(e))
            
        # 6. Apply state change
        recommendation.status = new_status
        await self.repository.save(recommendation)
        
        # 7. Create Audit Decision Record
        decision_record = ApprovalDecision(
            recommendation_id=recommendation.id,
            decision=request.decision,
            decided_by_user_id=user_id,
            decided_by_role=role,
            justification=request.justification
        )
        
        # 8. Log Audit Event
        await self.audit_logger.log_event(
            action=f"RECOMMENDATION_{target_status.value.upper()}",
            actor_id=user_id,
            details=f"Recommendation {recommendation_id} set to {target_status.value}. Reason: {request.justification}"
        )
        
        return ProcessApprovalResponse(
            recommendation_id=recommendation.id,
            new_status=new_status
        )
