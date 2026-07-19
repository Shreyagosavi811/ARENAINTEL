from enum import Enum

class WeatherCondition(str, Enum):
    CLEAR = "clear"
    RAIN = "rain"
    SNOW = "snow"
    EXTREME_HEAT = "extreme_heat"
    STORM = "storm"

class IncidentSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class IncidentType(str, Enum):
    MEDICAL = "medical"
    CROWD = "crowd"
    SECURITY = "security"
    FACILITY = "facility"
    WEATHER = "weather"
