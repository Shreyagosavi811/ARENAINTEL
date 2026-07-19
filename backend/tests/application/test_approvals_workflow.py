import pytest
from uuid import uuid4
from fastapi import HTTPException
from app.application.approvals.schemas import ProcessApprovalRequest
from app.application.approvals.process_approval import ProcessApprovalUseCase
from app.infrastructure.persistence.repository import MockRecommendationRepository
from app.domain.models.ai import AIRecommendation, RiskAssessment, AIMetadata
from app.domain.enums.ai import ApprovalDecisionType, RecommendationStatus, ConfidenceLevel
from app.domain.enums.operations import IncidentSeverity

class MockAuditLogger:
    def __init__(self):
        self.logs = []
    async def log_event(self, action, actor_id, details):
        self.logs.append({"action": action, "actor": actor_id, "details": details})

@pytest.fixture
def repo():
    return MockRecommendationRepository()

@pytest.fixture
def audit():
    return MockAuditLogger()

@pytest.fixture
def use_case(repo, audit):
    return ProcessApprovalUseCase(repository=repo, audit_logger=audit)

def create_pending_rec():
    meta = AIMetadata(source_model="test", confidence=ConfidenceLevel.HIGH, generation_time_ms=10)
    risk = RiskAssessment(assessed_severity=IncidentSeverity.HIGH, key_risk_factors=["test"], ai_metadata=meta)
    return AIRecommendation(incident_id=uuid4(), risk_assessment=risk)

@pytest.mark.asyncio
async def test_unauthenticated_cannot_approve(use_case):
    with pytest.raises(HTTPException) as exc:
        await use_case.execute(uuid4(), ProcessApprovalRequest(decision=ApprovalDecisionType.APPROVE), None, None)
    assert exc.value.status_code == 401
    
@pytest.mark.asyncio
async def test_unauthorized_cannot_approve(use_case, repo):
    rec = create_pending_rec()
    await repo.save(rec)
    
    with pytest.raises(HTTPException) as exc:
        await use_case.execute(rec.id, ProcessApprovalRequest(decision=ApprovalDecisionType.APPROVE), "user1", "operator")
    assert exc.value.status_code == 403
    
@pytest.mark.asyncio
async def test_ai_cannot_approve_its_own_output(use_case, repo):
    rec = create_pending_rec()
    await repo.save(rec)
    
    with pytest.raises(HTTPException) as exc:
        await use_case.execute(rec.id, ProcessApprovalRequest(decision=ApprovalDecisionType.APPROVE), "ai_bot", "ai")
    assert exc.value.status_code == 403

@pytest.mark.asyncio
async def test_successful_approval_creates_audit_event(use_case, repo, audit):
    rec = create_pending_rec()
    await repo.save(rec)
    
    req = ProcessApprovalRequest(decision=ApprovalDecisionType.APPROVE, justification="Looks good")
    res = await use_case.execute(rec.id, req, "super1", "supervisor")
    
    assert res.new_status == RecommendationStatus.APPROVED
    
    updated_rec = await repo.get(rec.id)
    assert updated_rec.status == RecommendationStatus.APPROVED
    
    assert len(audit.logs) == 1
    assert audit.logs[0]["action"] == "RECOMMENDATION_APPROVED"

@pytest.mark.asyncio
async def test_rejected_cannot_be_executed(use_case, repo):
    rec = create_pending_rec()
    await repo.save(rec)
    
    # Reject it
    req1 = ProcessApprovalRequest(decision=ApprovalDecisionType.REJECT)
    await use_case.execute(rec.id, req1, "super1", "supervisor")
    
    # Attempt to transition Rejected to Approved/Executed
    req2 = ProcessApprovalRequest(decision=ApprovalDecisionType.APPROVE)
    with pytest.raises(HTTPException) as exc:
        await use_case.execute(rec.id, req2, "super1", "supervisor")
    assert exc.value.status_code == 400
    assert "Cannot transition from rejected to approved" in exc.value.detail
