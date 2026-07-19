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

      {/* 1. MATCHDAY STATUS */}
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

      {/* 2. CRITICAL METRICS */}
      <section className="metric-grid" aria-label="Key Metrics">
        <div className="metric-card nominal" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-xs)' }}>
            <div className="metric-label">Stadium Occupancy</div>
            <div className="metric-value">45,210 <span style={{fontSize: '1rem', color: 'var(--text-muted)'}}>/ 65,000</span></div>
          </div>
          <div aria-label="Occupancy trend: increased from 42,100 to 45,210 over the last 60 minutes" style={{ marginTop: 'auto' }}>
            <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '4px' }}>SIMULATED OCCUPANCY · LAST 60 MIN</div>
            <div style={{ display: 'flex', alignItems: 'flex-end', height: '30px', gap: '4px' }} aria-hidden="true">
              <div style={{ flex: 1, background: 'var(--text-muted)', opacity: 0.3, height: '40%', borderRadius: '2px 2px 0 0' }}></div>
              <div style={{ flex: 1, background: 'var(--text-muted)', opacity: 0.5, height: '60%', borderRadius: '2px 2px 0 0' }}></div>
              <div style={{ flex: 1, background: 'var(--text-muted)', opacity: 0.7, height: '80%', borderRadius: '2px 2px 0 0' }}></div>
              <div style={{ flex: 1, background: 'var(--status-nominal)', height: '100%', borderRadius: '2px 2px 0 0' }}></div>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.7rem', color: 'var(--text-muted)', marginTop: '2px' }} aria-hidden="true">
              <span>42.1k</span>
              <span style={{ color: 'var(--status-nominal)' }}>45.2k</span>
            </div>
          </div>
        </div>
        <div className="metric-card warning" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-xs)' }}>
          <div className="metric-label">Active Incidents</div>
          <div className="metric-value text-warning">3</div>
        </div>
        <div className="metric-card warning" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-xs)' }}>
          <div className="metric-label">Pending Human Approvals</div>
          <div className="metric-value text-warning">2</div>
        </div>
        <div className="metric-card nominal" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-xs)' }}>
          <div className="metric-label">AI Inference Latency</div>
          <div className="metric-value">845ms</div>
        </div>
      </section>

      {/* 3 & 4. DECISIONS AND ACTIONS */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: 'var(--space-md)' }}>
        
        {/* RECENT AI-ASSISTED DECISIONS */}
        <section className="card" style={{ flex: 2 }}>
          <div className="card-header">
            <h3>Recent AI-Assisted Decisions</h3>
          </div>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <li style={{ padding: '1rem', background: 'var(--bg-app)', borderRadius: 'var(--radius-md)', borderLeft: '4px solid var(--status-warning)', display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '1px' }}>AI-ASSISTED DECISION</div>
              <strong style={{ fontSize: '1.1rem' }}>West Elevator Malfunction</strong>
              
              <div style={{ display: 'grid', gridTemplateColumns: '100px 1fr', gap: '0.25rem', fontSize: '0.85rem', marginTop: '0.25rem' }}>
                <span style={{ color: 'var(--text-muted)' }}>Risk:</span>
                <span className="text-warning" style={{ fontWeight: 'bold' }}>MEDIUM</span>
                
                <span style={{ color: 'var(--text-muted)' }}>Source:</span>
                <span>SOP Retrieval + GenAI Analysis</span>
                
                <span style={{ color: 'var(--text-muted)' }}>Status:</span>
                <div><span className="badge badge-warning" style={{ marginTop: '2px' }}>PENDING HUMAN APPROVAL</span></div>
              </div>
            </li>

            <li style={{ padding: '1rem', background: 'var(--bg-app)', borderRadius: 'var(--radius-md)', borderLeft: '4px solid var(--status-nominal)', display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '1px' }}>AI-ASSISTED DECISION</div>
              <strong style={{ fontSize: '1.1rem' }}>Gate C Crowd Surge</strong>
              
              <div style={{ display: 'grid', gridTemplateColumns: '100px 1fr', gap: '0.25rem', fontSize: '0.85rem', marginTop: '0.25rem' }}>
                <span style={{ color: 'var(--text-muted)' }}>Risk:</span>
                <span className="text-critical" style={{ fontWeight: 'bold' }}>HIGH</span>
                
                <span style={{ color: 'var(--text-muted)' }}>Source:</span>
                <span>SOP Retrieval + GenAI Analysis</span>
                
                <span style={{ color: 'var(--text-muted)' }}>Status:</span>
                <div><span className="badge badge-nominal" style={{ marginTop: '2px' }}>APPROVED BY SUPERVISOR</span></div>
              </div>
            </li>
          </ul>
        </section>

        {/* QUICK ACTIONS */}
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

      </div>
    </div>
  );
};
