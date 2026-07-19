from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from ..enums.ai import ApprovalDecisionType

class ApprovalDecision(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    recommendation_id: UUID
    decision: ApprovalDecisionType
    decided_by_user_id: str
    decided_by_role: str
    justification: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class AuditEvent(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    action: str
    actor_id: str
    entity_id: UUID
    entity_type: str
    details: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
