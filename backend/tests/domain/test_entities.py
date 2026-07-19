import pytest
from pydantic import ValidationError
from app.domain.models.entities import Stadium, Gate
from app.domain.enums.entities import GateStatus

def test_valid_stadium():
    s = Stadium(name="Grand Arena", capacity=50000, current_occupancy=25000)
    assert s.name == "Grand Arena"
    assert s.capacity == 50000

def test_invalid_stadium_capacity():
    with pytest.raises(ValidationError):
        Stadium(name="Arena", capacity=-100) # Boundary: capacity must be > 0

def test_invalid_stadium_occupancy():
    with pytest.raises(ValidationError):
        Stadium(name="Arena", capacity=100, current_occupancy=-1) # Boundary: ge=0

def test_gate_default_status():
    s = Stadium(name="A", capacity=100)
    g = Gate(stadium_id=s.id, name="North Gate")
    assert g.status == GateStatus.CLOSED
