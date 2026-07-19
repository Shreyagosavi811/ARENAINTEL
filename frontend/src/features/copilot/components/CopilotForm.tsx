import React, { useState } from 'react'
import { CopilotResults } from './CopilotResults'
import { useCopilotAnalysis } from '../hooks/useCopilotAnalysis'
import { LoadingState, ErrorState, EmptyState } from '../../../components/States'

const EXAMPLES = [
  "West elevator in Section B is stuck. Heavy rain expected in 20 minutes.",
  "Large crowd forming at Gate C, scanners are offline."
];

export const CopilotForm: React.FC = () => {
  const [query, setQuery] = useState('')
  const { mutate, data, isPending, isError, error } = useCopilotAnalysis()

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (query.length < 10) return;
    mutate(query)
  }

  return (
    <section aria-labelledby="copilot-heading">
      <header style={{ padding: 0, background: 'transparent', border: 'none', marginBottom: '1.5rem' }}>
        <h2 id="copilot-heading" style={{ margin: 0, fontSize: '1.75rem' }}>Operations Copilot</h2>
        <p style={{ color: 'var(--text-muted)', margin: '0.5rem 0 0 0' }}>Submit observational reports for instant SOP retrieval and AI risk analysis.</p>
      </header>

      <form onSubmit={handleSubmit} className="card">
        <div style={{ display: 'flex', gap: '8px', marginBottom: 'var(--space-md)', flexWrap: 'wrap' }}>
          {EXAMPLES.map(ex => (
            <button key={ex} type="button" onClick={() => setQuery(ex)} className="badge badge-neutral" style={{cursor: 'pointer', background: 'var(--bg-surface-elevated)'}}>
              {ex}
            </button>
          ))}
        </div>

        <div className="form-group">
          <label htmlFor="copilot-query">
            <span>Operational Situation</span>
            <span className={`char-count ${query.length > 2000 ? 'text-critical' : ''}`}>{query.length} / 2000</span>
          </label>
          <textarea
            id="copilot-query"
            className="form-control"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            aria-required="true"
            aria-invalid={query.length > 0 && (query.length < 10 || query.length > 2000)}
            disabled={isPending}
            rows={5}
          />
        </div>
        
        <button type="submit" className="btn btn-primary" disabled={query.length < 10 || query.length > 2000 || isPending}>
          {isPending && <span className="spinner" aria-hidden="true" style={{marginRight: '8px'}}></span>}
          {isPending ? 'Analyzing...' : 'Submit for Analysis'}
        </button>
      </form>
      
      <div style={{ marginTop: '2rem' }}>
        {isPending && <LoadingState message="Retrieving Knowledge Base SOPs..." />}
        {isError && <ErrorState error={error} onRetry={() => mutate(query)} />}
        {!isPending && !isError && !data && query.length === 0 && <EmptyState message="Enter an operational situation to begin analysis." />}
        {data && <CopilotResults results={data} originalInput={query} />}
      </div>
    </section>
  )
}
