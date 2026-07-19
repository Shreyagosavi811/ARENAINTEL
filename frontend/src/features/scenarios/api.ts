import { apiClient } from "../../services/apiClient";
import type { ScenarioSimulationResponse } from "./types";

export const simulateScenario = async (text: string): Promise<ScenarioSimulationResponse> => {
  const { data } = await apiClient.post<ScenarioSimulationResponse>("/scenarios/simulate", { query: text });
  return data;
};
