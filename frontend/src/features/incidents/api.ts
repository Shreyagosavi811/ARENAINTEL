import { apiClient } from "../../services/apiClient";
import type { ReportIncidentResponse } from "./types";

export const reportIncident = async (payload: { description: string; category: string; location: string }): Promise<ReportIncidentResponse> => {
  const { data } = await apiClient.post<ReportIncidentResponse>("/incidents/report", payload);
  return data;
};
