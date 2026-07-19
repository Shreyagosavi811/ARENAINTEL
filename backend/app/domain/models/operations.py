from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime
from ..enums.operations import WeatherCondition, IncidentSeverity, IncidentType
from .entities import Stadium, Gate, Facility, MedicalUnit, Match

class WeatherState(BaseModel):
    condition: WeatherCondition
    temperature_celsius: float
    wind_speed_kmh: float
    recorded_at: datetime = Field(default_factory=datetime.utcnow)

class OperationalIncident(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    type: IncidentType
    severity: IncidentSeverity
    description: str = Field(..., min_length=10)
    location: str
    reported_at: datetime = Field(default_factory=datetime.utcnow)
    resolved_at: Optional[datetime] = None
    is_resolved: bool = False

class OperationalContext(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    stadium: Stadium
    active_match: Optional[Match] = None
    weather: WeatherState
    gates: List[Gate]
    facilities: List[Facility]
    medical_units: List[MedicalUnit]
    active_incidents: List[OperationalIncident]
