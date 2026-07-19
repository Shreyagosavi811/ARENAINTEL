import React from 'react';
import { MatchdayStatus } from './MatchdayStatus';
import { CriticalMetrics } from './CriticalMetrics';
import { RecentDecisions } from './RecentDecisions';
import { QuickActions } from './QuickActions';

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

      <MatchdayStatus />
      <CriticalMetrics />

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: 'var(--space-md)' }}>
        <RecentDecisions />
        <QuickActions onNavigate={onNavigate} />
      </div>
    </div>
  );
};
