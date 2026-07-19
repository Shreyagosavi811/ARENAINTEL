import React from 'react';
import type { ScenarioSimulationResponse } from '../types';

interface Props {
  results: ScenarioSimulationResponse;
}

export const ScenarioSimulation: React.FC<Props> = ({ results }) => {
  return (
    <div className="card sandbox-boundary">
      <div style={{ position: 'absolute', width: '1px', height: '1px', padding: 0, margin: '-1px', overflow: 'hidden', clip: 'rect(0, 0, 0, 0)', whiteSpace: 'nowrap', borderWidth: 0 }}>
        HYPOTHETICAL SIMULATION - NO LIVE STATE MODIFIED
      </div>
      <h3 id="scenario-title" style={{ marginTop: '0' }}>Query: {results.scenario_query}</h3>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
        <div style={{ background: 'var(--bg-app)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)' }}>
          <h4 style={{ margin: '0 0 var(--space-sm) 0' }}>Expected Impacts</h4>
          <ul style={{ margin: 0, paddingLeft: '20px' }}>
            {results.expected_impacts.map((impact) => <li key={impact}>{impact}</li>)}
          </ul>
        </div>

        <div style={{ background: 'var(--bg-app)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)' }}>
          <h4 style={{ margin: '0 0 var(--space-sm) 0' }}>Recommended Mitigations</h4>
          <ul style={{ margin: 0, paddingLeft: '20px' }}>
            {results.mitigations.map((m) => <li key={m.action}><strong>{m.action}</strong>: {m.impact}</li>)}
          </ul>
        </div>

        <div style={{ background: 'var(--bg-app)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)', borderLeft: '4px solid var(--status-warning)' }}>
          <h4 style={{ margin: '0 0 var(--space-sm) 0' }}>Assumptions & Uncertainties</h4>
          <p style={{ margin: '0 0 var(--space-xs) 0' }}><strong>Assumptions:</strong> {results.assumptions.join(", ")}</p>
          <p style={{ margin: 0 }}><strong>Uncertainty:</strong> {results.uncertainty}</p>
        </div>
      </div>
      
      <p className="text-muted" style={{ marginTop: 'var(--space-lg)', fontStyle: 'italic', fontSize: '0.85rem' }}>
        * The AI may present estimates and probabilities. These are hypothetical projections, not guaranteed outcomes.
      </p>
    </div>
  );
};
