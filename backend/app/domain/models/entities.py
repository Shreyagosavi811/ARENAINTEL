from pydantic import BaseModel, Field, conint
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime
from ..enums.entities import GateStatus, FacilityStatus, MedicalUnitStatus, VolunteerRole

class Stadium(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., min_length=1)
    capacity: conint(gt=0)
    current_occupancy: conint(ge=0) = 0

class Gate(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    stadium_id: UUID
    name: str = Field(..., min_length=1)
    status: GateStatus = GateStatus.CLOSED
    flow_rate_per_minute: conint(ge=0) = 0

class Facility(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    stadium_id: UUID
    name: str
    facility_type: str
    status: FacilityStatus = FacilityStatus.OPERATIONAL

class MedicalUnit(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    stadium_id: UUID
    location_description: str
    status: MedicalUnitStatus = MedicalUnitStatus.AVAILABLE
    staff_count: conint(ge=0) = 0

class AccessibilityRoute(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    stadium_id: UUID
    start_point: str
    end_point: str
    is_active: bool = True

class Volunteer(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    role: VolunteerRole
    is_active: bool = True
    assigned_location: Optional[str] = None

class Match(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    stadium_id: UUID
    home_team: str
    away_team: str
    scheduled_start: datetime
    actual_start: Optional[datetime] = None
    is_finished: bool = False
