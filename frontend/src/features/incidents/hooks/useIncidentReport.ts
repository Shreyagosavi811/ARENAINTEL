import { useMutation } from "@tanstack/react-query";
import { reportIncident } from "../api";
import type { ReportIncidentResponse } from "../types";

export const useIncidentReport = () => {
  return useMutation<ReportIncidentResponse, Error, { description: string; category: string; location: string }>({
    mutationFn: (payload) => reportIncident(payload)
  });
};
