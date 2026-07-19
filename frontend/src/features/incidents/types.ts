export interface IncidentAIResponse {
  incident_category: string;
  location: string;
  severity_assessment: string;
  missing_information: string[];
  recommended_steps: string[];
  required_resources: string[];
  communication_draft?: string;
  requires_human_approval: boolean;
}

export interface ReportIncidentResponse {
  is_medical_diagnosis: boolean;
  ai_analysis: IncidentAIResponse;
}
