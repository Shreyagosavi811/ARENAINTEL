import pytest
from app.domain.enums.ai import RecommendationStatus
from app.domain.rules.state_machine import transition_recommendation, InvalidStateTransitionError

def test_valid_transitions():
    assert transition_recommendation(RecommendationStatus.PENDING_REVIEW, RecommendationStatus.APPROVED) == RecommendationStatus.APPROVED
    assert transition_recommendation(RecommendationStatus.PENDING_REVIEW, RecommendationStatus.REJECTED) == RecommendationStatus.REJECTED
    assert transition_recommendation(RecommendationStatus.APPROVED, RecommendationStatus.EXECUTED) == RecommendationStatus.EXECUTED

def test_invalid_transitions():
    with pytest.raises(InvalidStateTransitionError):
        transition_recommendation(RecommendationStatus.PENDING_REVIEW, RecommendationStatus.EXECUTED)
    
    with pytest.raises(InvalidStateTransitionError):
        transition_recommendation(RecommendationStatus.REJECTED, RecommendationStatus.APPROVED)
        
    with pytest.raises(InvalidStateTransitionError):
        transition_recommendation(RecommendationStatus.EXECUTED, RecommendationStatus.APPROVED)
