from pydantic import BaseModel
from ..enums.core import RecommendationState, RiskLevel

class AIAnalysis(BaseModel):
    risk_level: RiskLevel
    confidence: str

class Recommendation(BaseModel):
    id: str = "123"
    state: RecommendationState = RecommendationState.GENERATED
    analysis: AIAnalysis
