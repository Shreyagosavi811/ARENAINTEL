from enum import Enum

class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class RecommendationState(str, Enum):
    GENERATED = "generated"
    APPROVED = "approved"
