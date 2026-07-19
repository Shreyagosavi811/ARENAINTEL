import React from 'react';
import type { ReportIncidentResponse } from '../types';
import { Alert } from '../../../components/Alert';
import { ApprovalPanel } from '../../approvals/components/ApprovalPanel';

interface Props {
  results: ReportIncidentResponse;
  originalInput?: string;
}

export const ReportIncident: React.FC<Props> = ({ results, originalInput }) => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
      {results.is_medical_diagnosis && (
        <Alert variant="danger" icon="🏥">
          WARNING: AI cannot issue medical diagnoses. Always dispatch certified emergency medical services immediately based on observed symptoms.
        </Alert>
      )}

      <div className="card" style={{ borderLeft: '4px solid var(--text-muted)' }}>
        <h3 style={{ fontSize: '0.85rem', textTransform: 'uppercase', color: 'var(--text-muted)', margin: '0 0 8px 0' }}>📝 Reported Facts</h3>
        <p style={{ margin: 0, fontStyle: 'italic' }}>"{originalInput}"</p>
      </div>

      <div className="card" style={{ borderLeft: '4px solid var(--status-warning)', background: 'rgba(245, 158, 11, 0.05)' }}>
        <h3 style={{ margin: '0 0 var(--space-sm) 0', color: 'var(--status-warning)' }}>⚠️ AI-Identified Gaps</h3>
        <ul style={{ margin: 0, paddingLeft: '20px' }}>
          {results.ai_analysis.missing_information.map(info => <li key={info}>{info}</li>)}
        </ul>
      </div>

      <div className="card ai-boundary">
        <div className="flex-between" style={{ marginBottom: '1rem' }}>
          <h3 style={{ margin: 0 }}>✨ AI-Generated Response Plan</h3>
          <span className="badge badge-critical">{results.ai_analysis.severity_assessment} SEVERITY</span>
        </div>
        
        <div style={{ background: 'var(--bg-app)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)', marginBottom: 'var(--space-md)' }}>
          <h4 style={{ margin: '0 0 var(--space-sm) 0' }}>Recommended Steps</h4>
          <ul style={{ margin: 0, paddingLeft: '20px' }}>
            {results.ai_analysis.recommended_steps.map(step => <li key={step}>{step}</li>)}
          </ul>
        </div>

        <div style={{ background: 'var(--bg-app)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)' }}>
          <h4 style={{ margin: '0 0 var(--space-sm) 0' }}>Required Resources</h4>
          <ul style={{ margin: 0, paddingLeft: '20px' }}>
            {results.ai_analysis.required_resources.map(res => <li key={res}>{res}</li>)}
          </ul>
        </div>
      </div>

      {results.ai_analysis.requires_human_approval && <ApprovalPanel canApprove={true} />}
    </div>
  );
};
