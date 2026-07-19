import { useMutation } from "@tanstack/react-query";
import { simulateScenario } from "../api";
import type { ScenarioSimulationResponse } from "../types";

export const useScenarioSimulation = () => {
  return useMutation<ScenarioSimulationResponse, Error, string>({
    mutationFn: (text: string) => simulateScenario(text)
  });
};
