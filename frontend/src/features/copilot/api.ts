import { apiClient } from "../../services/apiClient";
import type { AnalyzeSituationResponse } from "./types";

export const analyzeSituation = async (text: string): Promise<AnalyzeSituationResponse> => {
  const { data } = await apiClient.post<AnalyzeSituationResponse>("/copilot/analyze", { text });
  return data;
};
