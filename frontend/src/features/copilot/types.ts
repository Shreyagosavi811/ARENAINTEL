export interface AIRecommendationAction {
  action: string;
  priority: string;
  reason: string;
  requires_approval: boolean;
}

export interface ActionCapabilities {
  can_approve: boolean;
  can_execute: boolean;
}

export interface OperationalImpact {
  potential_outcome: string;
  estimated_response_time_saved: string;
  affected_zones: string[];
  risk_trajectory: string;
  confidence: string;
  basis: string;
}

export interface AnalyzeSituationResponse {
  summary: string;
  risk_level: string;
  risks: string[];
  recommendations: AIRecommendationAction[];
  uncertainties: string[];
  sources: string[];
  retrieval_confidence: string;
  impact_estimate: OperationalImpact;
  capabilities: ActionCapabilities;
}
