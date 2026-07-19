import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import { CopilotResults } from "../src/features/copilot/components/CopilotResults";
import type { AnalyzeSituationResponse } from "../src/features/copilot/types";

describe("CopilotResults component", () => {
  it("renders pending approval status", () => {
    const mockData: AnalyzeSituationResponse = {
      summary: "Test",
      risk_level: "high",
      risks: [],
      recommendations: [
        { action: "Close Gate", priority: "High", reason: "Rain", requires_approval: true }
      ],
      uncertainties: [],
      sources: [],
      capabilities: { can_approve: true, can_execute: false }
    };

    render(<CopilotResults results={mockData} originalInput="Input" />);
    expect(screen.getByText(/PENDING HUMAN APPROVAL/i)).toBeDefined();
    expect(screen.getByText(/Authorize Plan/i)).toBeDefined(); // Approval Panel renders
  });
});
