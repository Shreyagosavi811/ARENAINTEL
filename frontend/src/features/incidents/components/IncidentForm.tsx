import React, { useState } from 'react'
import { ReportIncident } from './ReportIncident'
import { Alert } from '../../../components/Alert'
import { useIncidentReport } from '../hooks/useIncidentReport'
import { LoadingState, ErrorState, EmptyState } from '../../../components/States'

export const IncidentForm: React.FC = () => {
  const [desc, setDesc] = useState('')
  const [cat, setCat] = useState('Security')
  const [loc, setLoc] = useState('')
  const { mutate, data, isPending, isError, error } = useIncidentReport()

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (desc.length < 5) return;
    mutate({ description: desc, category: cat, location: loc })
  }

  return (
    <section aria-labelledby="incident-heading">
      <header style={{ padding: 0, background: 'transparent', border: 'none', marginBottom: '1.5rem' }}>
        <h2 id="incident-heading" style={{ margin: 0, fontSize: '1.75rem', color: 'var(--status-critical)' }}>Report Emergency Incident</h2>
      </header>

      <form onSubmit={handleSubmit} className="card" style={{ border: '1px solid var(--status-critical)' }}>
        <Alert variant="danger" icon="🚨">
          For immediate life-threatening emergencies, bypass this system and dispatch EMS/Police directly.
        </Alert>
        
        <div style={{ display: 'flex', gap: 'var(--space-md)', marginTop: 'var(--space-md)' }}>
          <div className="form-group" style={{ flex: 1 }}>
            <label>Category</label>
            <select className="form-control" value={cat} onChange={e => setCat(e.target.value)} disabled={isPending}>
              <option>Security</option>
              <option>Medical</option>
              <option>Maintenance</option>
            </select>
          </div>
          <div className="form-group" style={{ flex: 1 }}>
            <label>Location</label>
            <input className="form-control" value={loc} onChange={e => setLoc(e.target.value)} placeholder="e.g. Gate B" disabled={isPending} />
          </div>
        </div>

        <div className="form-group">
          <label>Incident Description (Facts only)</label>
          <textarea
            className="form-control"
            value={desc}
            onChange={(e) => setDesc(e.target.value)}
            rows={4}
            required
            minLength={5}
            disabled={isPending}
          />
        </div>
        
        <button type="submit" className="btn btn-danger" disabled={desc.length < 5 || isPending}>
          {isPending && <span className="spinner" aria-hidden="true" style={{marginRight: '8px'}}></span>}
          {isPending ? 'Processing Report...' : 'Submit Structured Report'}
        </button>
      </form>
      
      <div style={{ marginTop: '2rem' }} aria-live="polite">
        {isPending && <LoadingState message="Analyzing incident severity and generating response plan..." />}
        {isError && <ErrorState error={error} onRetry={() => mutate({ description: desc, category: cat, location: loc })} />}
        {!isPending && !isError && !data && desc.length === 0 && <EmptyState message="Fill out the incident form to receive an AI-assisted response plan." />}
        {data && <ReportIncident results={data} originalInput={`[${cat}] @ ${loc || 'Unknown'}: ${desc}`} />}
      </div>
    </section>
  )
}
