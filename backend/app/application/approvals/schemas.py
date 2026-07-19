from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from ...domain.enums.ai import ApprovalDecisionType, RecommendationStatus

class ProcessApprovalRequest(BaseModel):
    decision: ApprovalDecisionType
    justification: Optional[str] = None

class ProcessApprovalResponse(BaseModel):
    recommendation_id: UUID
    new_status: RecommendationStatus
