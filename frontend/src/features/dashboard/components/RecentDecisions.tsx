import React from 'react';

export const RecentDecisions: React.FC = () => {
  return (
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
  );
};
