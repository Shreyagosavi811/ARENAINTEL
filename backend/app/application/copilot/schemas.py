from pydantic import BaseModel, Field
from typing import List
from uuid import UUID

class AnalyzeSituationRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=2000)

class AIRecommendationAction(BaseModel):
    action: str
    priority: str
    reason: str
    requires_approval: bool = True

class CopilotAIResponse(BaseModel):
    summary: str
    risk_level: str
    risks: List[str]
    recommendations: List[AIRecommendationAction]
    uncertainties: List[str]

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
    capabilities: ActionCapabilities
