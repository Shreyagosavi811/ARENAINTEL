import pytest
from pydantic import ValidationError
from app.domain.models.operations import OperationalIncident, WeatherState
from app.domain.enums.operations import IncidentType, IncidentSeverity, WeatherCondition

def test_valid_incident():
    inc = OperationalIncident(
        type=IncidentType.CROWD,
        severity=IncidentSeverity.HIGH,
        description="Massive crowd surging at gate 3",
        location="Gate 3"
    )
    assert inc.is_resolved is False

def test_invalid_incident_description():
    with pytest.raises(ValidationError):
        # Boundary: min length 10
        OperationalIncident(
            type=IncidentType.CROWD,
            severity=IncidentSeverity.HIGH,
            description="Short",
            location="Gate 3"
        )
