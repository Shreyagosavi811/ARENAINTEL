import pytest
from uuid import uuid4
from pydantic import ValidationError
from app.domain.models.ai import AIRecommendation, RiskAssessment, AIMetadata
from app.domain.enums.ai import RecommendationStatus, ConfidenceLevel
from app.domain.enums.operations import IncidentSeverity

def test_valid_ai_recommendation():
    meta = AIMetadata(source_model="gpt-4", confidence=ConfidenceLevel.HIGH, generation_time_ms=1200)
    risk = RiskAssessment(assessed_severity=IncidentSeverity.CRITICAL, key_risk_factors=["Crush risk"], ai_metadata=meta)
    
    rec = AIRecommendation(
        incident_id=uuid4(),
        risk_assessment=risk
    )
    assert rec.status == RecommendationStatus.PENDING_REVIEW

def test_ai_output_cannot_be_executed():
    meta = AIMetadata(source_model="gpt-4", confidence=ConfidenceLevel.HIGH, generation_time_ms=1200)
    risk = RiskAssessment(assessed_severity=IncidentSeverity.CRITICAL, key_risk_factors=["Crush risk"], ai_metadata=meta)
    
    with pytest.raises(ValidationError, match="AI Recommendation cannot be initialized in EXECUTED state"):
        AIRecommendation(
            incident_id=uuid4(),
            status=RecommendationStatus.EXECUTED,
            risk_assessment=risk
        )
