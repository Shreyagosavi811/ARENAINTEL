import React, { useState } from 'react'
import { ScenarioSimulation } from './ScenarioSimulation'
import { useScenarioSimulation } from '../hooks/useScenarioSimulation'
import { LoadingState, ErrorState, EmptyState } from '../../../components/States'

const EXAMPLES = [
  "What if Gate B closes 20 minutes before kickoff?",
  "What if heavy rain begins immediately?"
];

export const ScenarioForm: React.FC = () => {
  const [query, setQuery] = useState('')
  const { mutate, data, isPending, isError, error, reset } = useScenarioSimulation()

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (query.length < 10) return;
    mutate(query)
  }

  const handleReset = () => {
    reset()
    setQuery('')
  }

  return (
    <section aria-labelledby="scenario-heading">
      <header style={{ padding: 0, background: 'transparent', border: 'none', marginBottom: '1.5rem' }}>
        <h2 id="scenario-heading" style={{ margin: 0, fontSize: '1.75rem' }}>What-If Simulator</h2>
        <p style={{ color: 'var(--text-muted)', margin: '0.5rem 0 0 0' }}>Safely simulate operational failures using cloned stadium telemetry.</p>
      </header>

      <form onSubmit={handleSubmit} className="card">
        <div style={{ marginBottom: 'var(--space-lg)', padding: 'var(--space-md)', background: 'var(--bg-app)', border: '1px solid var(--border-subtle)', borderRadius: 'var(--radius-md)', textAlign: 'center', fontFamily: 'monospace', color: 'var(--text-muted)' }}>
          <span style={{color: 'var(--status-nominal)'}}>🟢 LIVE STATE</span> ➡️ <span>🗄️ CLONED SANDBOX</span> ➡️ <span style={{color: 'var(--status-warning)'}}>⚠️ HYPOTHETICAL INJECTION</span>
        </div>

        <div style={{ display: 'flex', gap: '8px', marginBottom: 'var(--space-md)', flexWrap: 'wrap' }}>
          {EXAMPLES.map(ex => (
            <button key={ex} type="button" onClick={() => setQuery(ex)} className="badge badge-neutral" style={{cursor: 'pointer', background: 'var(--bg-surface-elevated)'}}>{ex}</button>
          ))}
        </div>

        <div className="form-group">
          <label htmlFor="scenario-query">Hypothetical Scenario</label>
          <textarea
            id="scenario-query"
            className="form-control"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            disabled={isPending}
            placeholder="e.g. What if..."
            rows={4}
          />
        </div>
        
        <div className="flex-between">
          <button type="submit" className="btn btn-primary" disabled={query.length < 10 || isPending}>
            {isPending && <span className="spinner" aria-hidden="true" style={{marginRight: '8px'}}></span>}
            {isPending ? 'Cloning State & Running...' : 'Run Simulation'}
          </button>
          {(data || isError) && !isPending && (
            <button type="button" className="btn btn-danger" onClick={handleReset}>Reset Sandbox</button>
          )}
        </div>
      </form>
      
      <div style={{ marginTop: '2rem' }} aria-live="polite">
        {isPending && <LoadingState message="Cloning live state and running isolated impact simulation..." />}
        {isError && <ErrorState error={error} onRetry={() => mutate(query)} />}
        {!isPending && !isError && !data && query.length === 0 && <EmptyState message="Enter a hypothetical scenario to begin sandbox simulation." />}
        {data && <ScenarioSimulation results={data} />}
      </div>
    </section>
  )
}
