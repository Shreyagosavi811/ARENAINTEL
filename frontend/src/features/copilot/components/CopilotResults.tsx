import React from 'react';
import type { AnalyzeSituationResponse } from '../types';
import { Alert } from '../../../components/Alert';
import { ApprovalPanel } from '../../approvals/components/ApprovalPanel';

interface Props {
  results: AnalyzeSituationResponse;
  originalInput: string;
}

export const CopilotResults: React.FC<Props> = ({ results, originalInput }) => {
  return (
    <div className="results-container" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }} aria-live="polite">
      <div className="card" style={{ borderLeft: '4px solid var(--text-muted)' }}>
        <h3 style={{ fontSize: '0.85rem', textTransform: 'uppercase', color: 'var(--text-muted)', margin: '0 0 8px 0' }}>Observed Input</h3>
        <p style={{ margin: 0, fontStyle: 'italic' }}>"{originalInput}"</p>
      </div>

      <div className="card">
        <div className="card-header">
          <h3>Retrieved Knowledge Base Sources</h3>
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px', background: 'var(--bg-surface-elevated)', padding: '8px', borderRadius: '4px' }}>
          <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>RETRIEVAL CONFIDENCE</span>
          <span style={{ color: 'var(--status-ai)', fontWeight: 'bold', fontSize: '0.9rem' }}>{results.retrieval_confidence || 'High'}</span>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          {results.sources.map(src => (
            <div key={src} style={{ background: 'var(--bg-app)', padding: '8px 12px', borderRadius: '4px', border: '1px solid var(--border-subtle)', fontSize: '0.85rem', color: 'var(--text-muted)' }}>
              <code style={{ color: 'var(--status-ai)', fontWeight: 'bold' }}>SOP MATCH</code> {src}
            </div>
          ))}
        </div>
      </div>
      
      {results.impact_estimate && (
        <div className="card" style={{ background: 'var(--bg-surface-elevated)', border: '1px solid var(--status-ai)' }}>
          <h3 style={{ margin: '0 0 1rem 0', color: 'var(--status-ai)', fontSize: '1rem', textTransform: 'uppercase', letterSpacing: '1px' }}>OPERATIONAL IMPACT — AI ESTIMATE</h3>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginBottom: '1rem' }}>
            <div>
              <strong style={{ display: 'block', fontSize: '0.8rem', color: 'var(--text-muted)' }}>Potential Outcome</strong>
              <span style={{ fontSize: '1.1rem' }}>{results.impact_estimate.potential_outcome}</span>
            </div>
            <div>
              <strong style={{ display: 'block', fontSize: '0.8rem', color: 'var(--text-muted)' }}>Estimated Response Time</strong>
              <span style={{ fontSize: '1.1rem' }}>{results.impact_estimate.estimated_response_time_saved} saved</span>
            </div>
            <div>
              <strong style={{ display: 'block', fontSize: '0.8rem', color: 'var(--text-muted)' }}>Affected Zones</strong>
              <span style={{ fontSize: '1.1rem' }}>{results.impact_estimate.affected_zones.join(' · ')}</span>
            </div>
            <div>
              <strong style={{ display: 'block', fontSize: '0.8rem', color: 'var(--text-muted)' }}>Risk Trajectory</strong>
              <span style={{ fontSize: '1.1rem' }}>{results.impact_estimate.risk_trajectory}</span>
            </div>
          </div>
          <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: '1rem', display: 'flex', gap: '2rem' }}>
            <div>
              <strong style={{ display: 'block', fontSize: '0.8rem', color: 'var(--text-muted)' }}>Confidence</strong>
              <span className={`badge badge-${results.impact_estimate.confidence.toLowerCase() === 'high' ? 'nominal' : 'warning'}`}>{results.impact_estimate.confidence}</span>
            </div>
            <div style={{ flex: 1 }}>
              <strong style={{ display: 'block', fontSize: '0.8rem', color: 'var(--text-muted)' }}>Basis</strong>
              <span style={{ fontSize: '0.9rem' }}>{results.impact_estimate.basis}</span>
            </div>
          </div>
        </div>
      )}

      <div className="card ai-boundary">
        <div className="flex-between" style={{ marginBottom: '1rem' }}>
          <h3 style={{ margin: 0 }}>Situation Analysis</h3>
          <div className={`badge badge-${results.risk_level.toLowerCase()}`}>
            RISK: {results.risk_level}
          </div>
        </div>
        
        <p style={{ fontSize: '1.1rem', lineHeight: '1.6', marginBottom: '1.5rem' }}>{results.summary}</p>

        {results.risks.length > 0 && (
          <div style={{ marginBottom: '1.5rem' }}>
            <h4 className="text-warning" style={{ margin: '0 0 8px 0' }}>Identified Risks</h4>
            <ul style={{ margin: 0, paddingLeft: '20px' }}>
              {results.risks.map(risk => <li key={risk}>{risk}</li>)}
            </ul>
          </div>
        )}

        <h4 style={{ margin: '0 0 8px 0', borderTop: '1px solid var(--border-subtle)', paddingTop: '1rem' }}>Recommended Actions</h4>
        {results.recommendations.some(r => r.requires_approval) && (
          <Alert variant="warning" icon="⚠️">
            The following actions require human authorization before execution. AI cannot execute infrastructure commands.
          </Alert>
        )}

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: 'var(--space-md)', marginTop: 'var(--space-md)' }}>
          {results.recommendations.map((rec) => (
            <div key={rec.action} style={{ background: 'var(--bg-app)', border: '1px solid var(--border-subtle)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)', display: 'flex', flexDirection: 'column' }}>
              <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '8px' }}>
                <h5 style={{ margin: 0, fontSize: '1rem' }}>{rec.action}</h5>
                <span className={`badge badge-${rec.priority.toLowerCase() === 'high' ? 'critical' : 'warning'}`}>{rec.priority}</span>
              </header>
              <p style={{ margin: '0 0 12px 0', fontSize: '0.9rem', color: 'var(--text-muted)', flex: 1 }}><strong>Reason:</strong> {rec.reason}</p>
              <div>
                {rec.requires_approval ? (
                  <span className="badge badge-warning">PENDING HUMAN APPROVAL</span>
                ) : (
                  <span className="badge badge-nominal">AUTO-EXECUTABLE</span>
                )}
              </div>
            </div>
          ))}
        </div>
        
        {results.capabilities.can_approve && <ApprovalPanel canApprove={results.capabilities.can_approve} />}
      </div>
    </div>
  );
};
