from pydantic import BaseModel, Field, model_validator
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime
from ..enums.ai import RecommendationStatus, ConfidenceLevel, ActionItemStatus
from ..enums.operations import IncidentSeverity

class AIMetadata(BaseModel):
    source_model: str
    confidence: ConfidenceLevel
    retrieved_context_ids: List[str] = Field(default_factory=list)
    generation_time_ms: int

class RiskAssessment(BaseModel):
    assessed_severity: IncidentSeverity
    key_risk_factors: List[str] = Field(min_length=1)
    estimated_impact_radius_meters: Optional[float] = None
    ai_metadata: AIMetadata

class ActionItem(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    description: str = Field(..., min_length=5)
    assigned_role: str
    target_location: Optional[str] = None
    status: ActionItemStatus = ActionItemStatus.PENDING

class CommunicationDraft(BaseModel):
    target_audience: str
    message: str = Field(..., min_length=1)
    channel: str

class AIRecommendation(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    incident_id: UUID
    status: RecommendationStatus = RecommendationStatus.PENDING_REVIEW
    risk_assessment: RiskAssessment
    action_items: List[ActionItem] = Field(default_factory=list)
    communication_drafts: List[CommunicationDraft] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: Optional[datetime] = None
    
    @model_validator(mode='after')
    def validate_not_executed(self):
        if self.status == RecommendationStatus.EXECUTED:
            raise ValueError("AI Recommendation cannot be initialized in EXECUTED state.")
        return self
