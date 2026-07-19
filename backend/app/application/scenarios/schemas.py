from pydantic import BaseModel, Field
from typing import List

class SimulateScenarioRequest(BaseModel):
    what_if_query: str = Field(..., min_length=10, max_length=2000)

class ScenarioMitigation(BaseModel):
    action: str
    impact: str

class ScenarioSimulationAIResponse(BaseModel):
    expected_impacts: List[str]
    potential_risks: List[str]
    mitigations: List[ScenarioMitigation]
    affected_stakeholders: List[str]
    communication_requirements: List[str]
    assumptions: List[str]
    uncertainty: str

class ScenarioSimulationResponse(BaseModel):
    scenario_query: str
    is_hypothetical_simulation: bool = True
    expected_impacts: List[str]
    potential_risks: List[str]
    mitigations: List[ScenarioMitigation]
    affected_stakeholders: List[str]
    communication_requirements: List[str]
    assumptions: List[str]
    uncertainty: str
    sources: List[str]
