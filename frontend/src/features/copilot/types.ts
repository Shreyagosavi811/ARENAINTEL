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

export interface AnalyzeSituationResponse {
  summary: string;
  risk_level: string;
  risks: string[];
  recommendations: AIRecommendationAction[];
  uncertainties: string[];
  sources: string[];
  capabilities: ActionCapabilities;
}
