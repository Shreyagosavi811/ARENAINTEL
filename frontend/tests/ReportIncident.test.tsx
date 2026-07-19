import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import { ReportIncident } from "../src/features/incidents/components/ReportIncident";
import type { ReportIncidentResponse } from "../src/features/incidents/types";

describe("ReportIncident component", () => {
  it("renders medical warning when flag is true", () => {
    const mockData: ReportIncidentResponse = {
      is_medical_diagnosis: true,
      ai_analysis: {
        incident_category: "Medical",
        location: "A",
        severity_assessment: "High",
        missing_information: [],
        recommended_steps: [],
        required_resources: [],
        requires_human_approval: false
      }
    };
    render(<ReportIncident results={mockData} />);
    expect(screen.getByText(/AI cannot issue medical diagnoses/i)).toBeDefined();
  });
});
