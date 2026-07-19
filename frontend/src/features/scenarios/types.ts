export interface ScenarioMitigation {
  action: string;
  impact: string;
}

export interface ScenarioSimulationResponse {
  scenario_query: string;
  is_hypothetical_simulation: boolean;
  expected_impacts: string[];
  potential_risks: string[];
  mitigations: ScenarioMitigation[];
  affected_stakeholders: string[];
  communication_requirements: string[];
  assumptions: string[];
  uncertainty: string;
  sources: string[];
}
