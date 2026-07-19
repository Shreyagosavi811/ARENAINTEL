import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import { ScenarioSimulation } from "../src/features/scenarios/components/ScenarioSimulation";
import { ScenarioSimulationResponse } from "../src/features/scenarios/types";

describe("ScenarioSimulation component", () => {
  it("renders the HYPOTHETICAL SIMULATION warning banner explicitly", () => {
    const mockData: ScenarioSimulationResponse = {
      scenario_query: "What if?",
      is_hypothetical_simulation: true,
      expected_impacts: ["A"],
      potential_risks: [],
      mitigations: [],
      affected_stakeholders: [],
      communication_requirements: [],
      assumptions: ["B"],
      uncertainty: "C",
      sources: []
    };

    render(<ScenarioSimulation results={mockData} />);
    expect(screen.getByText(/HYPOTHETICAL SIMULATION/i)).toBeDefined();
    expect(screen.getByText("Query: What if?")).toBeDefined();
  });
});
