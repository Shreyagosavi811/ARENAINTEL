from ..enums.ai import RecommendationStatus

class InvalidStateTransitionError(Exception):
    pass

def transition_recommendation(current: RecommendationStatus, target: RecommendationStatus) -> RecommendationStatus:
    valid_transitions = {
        RecommendationStatus.PENDING_REVIEW: {RecommendationStatus.APPROVED, RecommendationStatus.REJECTED},
        RecommendationStatus.APPROVED: {RecommendationStatus.EXECUTED},
        RecommendationStatus.REJECTED: set(),
        RecommendationStatus.EXECUTED: set()
    }
    
    allowed = valid_transitions.get(current, set())
    if target not in allowed:
        raise InvalidStateTransitionError(f"Cannot transition from {current.value} to {target.value}")
    
    return target
