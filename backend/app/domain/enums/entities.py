from enum import Enum

class GateStatus(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    CONGESTED = "congested"
    EMERGENCY_ONLY = "emergency_only"

class FacilityStatus(str, Enum):
    OPERATIONAL = "operational"
    MAINTENANCE = "maintenance"
    OUT_OF_SERVICE = "out_of_service"

class MedicalUnitStatus(str, Enum):
    AVAILABLE = "available"
    BUSY = "busy"
    OFFLINE = "offline"

class VolunteerRole(str, Enum):
    CROWD_CONTROL = "crowd_control"
    MEDICAL_ASSIST = "medical_assist"
    ACCESSIBILITY_SUPPORT = "accessibility_support"
    GENERAL_INFO = "general_info"
