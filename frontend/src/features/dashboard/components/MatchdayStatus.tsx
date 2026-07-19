import React from 'react';

export const MatchdayStatus: React.FC = () => {
  return (
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
  );
};
