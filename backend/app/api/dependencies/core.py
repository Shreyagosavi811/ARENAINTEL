from ...core.config import settings
from ...infrastructure.ai.provider import IAIProvider, MockAIProvider, BaseRealAIProvider
from ...infrastructure.retrieval.provider import IRetriever, MockRetriever
from ...infrastructure.audit.logger import AuditLogger
from ...infrastructure.persistence.repository import IRecommendationRepository, MockRecommendationRepository, SQLiteRecommendationRepository
from ...application.copilot.context_service import ContextService

_mock_repo = MockRecommendationRepository()
_sqlite_repo = SQLiteRecommendationRepository()
_audit_logger = AuditLogger()
_context_service = ContextService()

def get_ai_provider() -> IAIProvider:
    if settings.USE_MOCK_AI:
        return MockAIProvider()
    return BaseRealAIProvider() # Fallback for structural adherence, assumes real implementation

def get_retriever() -> IRetriever:
    return MockRetriever()

def get_audit_logger() -> AuditLogger:
    return _audit_logger

def get_recommendation_repository() -> IRecommendationRepository:
    # Use SQLite repo in production, but we can fall back to mock if needed
    return _sqlite_repo

def get_context_service() -> ContextService:
    return _context_service
