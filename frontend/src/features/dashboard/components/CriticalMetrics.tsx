import React from 'react';

export const CriticalMetrics: React.FC = () => {
  return (
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
  );
};
