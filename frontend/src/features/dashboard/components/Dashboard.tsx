import React from 'react';

interface Props {
  onNavigate: (tab: 'dashboard' | 'copilot' | 'scenarios' | 'incidents') => void;
}

export const Dashboard: React.FC<Props> = ({ onNavigate }) => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-xl)' }}>
      <header>
        <h2 style={{ fontSize: '2rem', margin: '0 0 var(--space-sm) 0' }}>Stadium Operations Overview</h2>
        <p className="text-muted" style={{ margin: 0 }}>Matchday operations intelligence using simulated operational inputs and AI-assisted decision support.</p>
      </header>

      {/* SIMULATED STATUS STRIP */}
      <section className="card" aria-label="Matchday Status" style={{ background: 'var(--bg-surface-elevated)', padding: 'var(--space-md)' }}>
        <h3 style={{ fontSize: '0.85rem', color: 'var(--text-muted)', letterSpacing: '1px', marginTop: 0, marginBottom: 'var(--space-sm)' }}>SIMULATED MATCHDAY STATUS</h3>
        <div style={{ display: 'flex', justifyContent: 'space-between', flexWrap: 'wrap', gap: '1rem' }}>
          <div><div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>GATES</div><strong>8 / 10 OPEN</strong></div>
          <div><div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>TRANSPORT</div><strong>NORMAL</strong></div>
          <div><div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>WEATHER</div><strong>MONITORED</strong></div>
          <div><div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>STAFFING</div><strong>STABLE</strong></div>
          <div><div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>NETWORK</div><strong style={{ color: 'var(--status-nominal)' }}>ONLINE</strong></div>
        </div>
      </section>

      <section className="metric-grid" aria-label="Key Metrics">
        <div className="metric-card nominal">
          <span className="metric-label">Stadium Occupancy</span>
          <span className="metric-value">45,210 <span style={{fontSize: '1rem', color: 'var(--text-muted)'}}>/ 65,000</span></span>
        </div>
        <div className="metric-card warning">
          <span className="metric-label">Active Incidents</span>
          <span className="metric-value text-warning">3</span>
        </div>
        <div className="metric-card warning">
          <span className="metric-label">Pending Human Approvals</span>
          <span className="metric-value text-warning">2</span>
        </div>
        <div className="metric-card nominal">
          <span className="metric-label">AI Inference Latency</span>
          <span className="metric-value">845ms</span>
        </div>
      </section>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: 'var(--space-md)' }}>
        <section className="card">
          <div className="card-header">
            <h3>Recent AI-Assisted Decisions</h3>
          </div>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <li style={{ padding: '1rem', background: 'var(--bg-app)', borderRadius: 'var(--radius-md)', borderLeft: '4px solid var(--status-warning)' }}>
              <strong>West Elevator Malfunction</strong>
              <div className="flex-between" style={{ marginTop: '0.5rem' }}>
                <span className="badge badge-warning">PENDING HUMAN APPROVAL</span>
                <span className="text-muted" style={{fontSize: '0.85rem'}}>2 mins ago</span>
              </div>
            </li>
            <li style={{ padding: '1rem', background: 'var(--bg-app)', borderRadius: 'var(--radius-md)', borderLeft: '4px solid var(--status-nominal)' }}>
              <strong>Gate C Crowd Surge</strong>
              <div className="flex-between" style={{ marginTop: '0.5rem' }}>
                <span className="badge badge-nominal">APPROVED BY SUPERVISOR</span>
                <span className="text-muted" style={{fontSize: '0.85rem'}}>15 mins ago</span>
              </div>
            </li>
          </ul>
        </section>

        <section className="card">
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
      </div>
    </div>
  );
};
