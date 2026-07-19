import React from 'react';

interface Props {
  onNavigate: (tab: 'dashboard' | 'copilot' | 'scenarios' | 'incidents') => void;
}

export const QuickActions: React.FC<Props> = ({ onNavigate }) => {
  return (
    <section className="card" style={{ flex: 1, alignSelf: 'start' }}>
      <div className="card-header">
        <h3>Quick Actions</h3>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        <button className="btn" onClick={() => onNavigate('copilot')}>
          Analyze Operational Situation (Copilot)
        </button>
        <button className="btn" onClick={() => onNavigate('scenarios')}>
          Run Hypothetical Sandbox (Simulation Only)
        </button>
        <button className="btn btn-danger" onClick={() => onNavigate('incidents')}>
          Report Operational Incident
        </button>
      </div>
    </section>
  );
};
