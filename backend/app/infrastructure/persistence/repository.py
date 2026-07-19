from typing import Dict, Optional, Protocol
from uuid import UUID
from sqlalchemy import create_engine, Column, String, JSON
from sqlalchemy.orm import declarative_base, sessionmaker
from ...domain.models.ai import AIRecommendation
from ...core.config import settings
import json

Base = declarative_base()

class DBRecommendation(Base):
    __tablename__ = "recommendations"
    id = Column(String, primary_key=True, index=True)
    status = Column(String, nullable=False)
    data_json = Column(JSON, nullable=False)

# Initialize engine
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class IRecommendationRepository(Protocol):
    async def get(self, id: UUID) -> Optional[AIRecommendation]:
        ...
    async def save(self, recommendation: AIRecommendation) -> AIRecommendation:
        ...

class SQLiteRecommendationRepository(IRecommendationRepository):
    async def get(self, id: UUID) -> Optional[AIRecommendation]:
        with SessionLocal() as db:
            record = db.query(DBRecommendation).filter(DBRecommendation.id == str(id)).first()
            if not record:
                return None
            return AIRecommendation.model_validate(record.data_json)
            
    async def save(self, recommendation: AIRecommendation) -> AIRecommendation:
        with SessionLocal() as db:
            record = db.query(DBRecommendation).filter(DBRecommendation.id == str(recommendation.id)).first()
            if not record:
                record = DBRecommendation(id=str(recommendation.id))
                db.add(record)
            
            record.status = recommendation.status.value
            record.data_json = recommendation.model_dump(mode="json")
            db.commit()
            return recommendation

class MockRecommendationRepository(IRecommendationRepository):
    def __init__(self):
        self._store: Dict[UUID, AIRecommendation] = {}
        
    async def get(self, id: UUID) -> Optional[AIRecommendation]:
        return self._store.get(id)
        
    async def save(self, recommendation: AIRecommendation) -> AIRecommendation:
        self._store[recommendation.id] = recommendation
        return recommendation
