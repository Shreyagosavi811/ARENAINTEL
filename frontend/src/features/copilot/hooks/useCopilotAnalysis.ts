import { useMutation } from "@tanstack/react-query";
import { analyzeSituation } from "../api";
import type { AnalyzeSituationResponse } from "../types";

export const useCopilotAnalysis = () => {
  return useMutation<AnalyzeSituationResponse, Error, string>({
    mutationFn: (text: string) => analyzeSituation(text)
  });
};
