from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID

class MatchdayContext(BaseModel):
    match: str = "Mexico vs Brazil"
    venue: str = "ARENAINTEL Stadium"
    phase: str = "Pre-Match"
    attendance: str = "58,420 / 62,000"
    weather: str = "Heavy Rain Expected"
    transport: str = "Metro Line 2 Delayed"

class AnalyzeSituationRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=2000)
    matchday_context: Optional[MatchdayContext] = None

class AIRecommendationAction(BaseModel):
    action: str
    priority: str
    reason: str
    requires_approval: bool = True

class OperationalImpact(BaseModel):
    potential_outcome: str
    estimated_response_time_saved: str
    affected_zones: List[str]
    risk_trajectory: str
    confidence: str
    basis: str

class CopilotAIResponse(BaseModel):
    summary: str
    risk_level: str
    risks: List[str]
    recommendations: List[AIRecommendationAction]
    uncertainties: List[str]
    impact_estimate: OperationalImpact

class ActionCapabilities(BaseModel):
    can_approve: bool
    can_execute: bool

class AnalyzeSituationResponse(BaseModel):
    summary: str
    risk_level: str
    risks: List[str]
    recommendations: List[AIRecommendationAction]
    uncertainties: List[str]
    sources: List[str]
    retrieval_confidence: str
    impact_estimate: OperationalImpact
    capabilities: ActionCapabilities
