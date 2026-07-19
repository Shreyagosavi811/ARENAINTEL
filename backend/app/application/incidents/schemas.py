from pydantic import BaseModel, Field
from typing import List, Optional

class ReportIncidentRequest(BaseModel):
    # Input validation: max 1000 chars to prevent massive injection payloads
    text: str = Field(..., min_length=5, max_length=1000)

class IncidentAIResponse(BaseModel):
    incident_category: str
    location: str
    severity_assessment: str
    missing_information: List[str]
    recommended_steps: List[str]
    required_resources: List[str]
    communication_draft: Optional[str] = None
    requires_human_approval: bool = True

class ReportIncidentResponse(BaseModel):
    is_medical_diagnosis: bool = False
    ai_analysis: IncidentAIResponse
