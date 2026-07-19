import React, { useState } from 'react'
import { CopilotForm } from './features/copilot/components/CopilotForm'
import { ScenarioForm } from './features/scenarios/components/ScenarioForm'
import { IncidentForm } from './features/incidents/components/IncidentForm'
import { Dashboard } from './features/dashboard/components/Dashboard'
import { ArenaIntelLogo } from './components/ArenaIntelLogo'

const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'dashboard' | 'copilot' | 'scenarios' | 'incidents'>('dashboard')

  return (
    <div className="app-layout">
      <a href="#main-content" className="skip-link">Skip to main content</a>
      
      <header role="banner" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-md)' }}>
          <ArenaIntelLogo size={45} />
          <div>
            <h1 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '4px' }}>
              ARENA<span style={{ color: 'var(--status-ai)' }}>INTEL</span>
            </h1>
            <p style={{ margin: 0, fontSize: '0.85rem', color: 'var(--text-muted)', letterSpacing: '1px' }}>
              FIFA WORLD CUP 2026 &bull; MATCHDAY OPERATIONS
            </p>
          </div>
        </div>
        <div className="flex-between gap-md" style={{ textAlign: 'right' }}>
          <div>
            <div style={{ fontSize: '0.8rem', fontWeight: 'bold' }}>METLIFE STADIUM</div>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>MATCHDAY 12 (SIMULATED)</div>
          </div>
          <span className="badge badge-nominal" style={{ marginLeft: '1rem' }}>SYSTEM ONLINE</span>
          <span className="badge badge-neutral">ADMIN USER</span>
        </div>
      </header>
      
      <div className="app-body">
        <nav role="navigation" aria-label="Main Navigation" className="sidebar">
          
          <div style={{ padding: '0 1rem', marginBottom: '0.5rem', fontSize: '0.75rem', fontWeight: 'bold', color: 'var(--text-muted)', letterSpacing: '1px' }}>MATCHDAY OPERATIONS</div>
          <ul style={{ marginBottom: '2rem' }}>
            <li>
              <button className="nav-btn" onClick={() => setActiveTab('dashboard')} aria-current={activeTab === 'dashboard' ? 'page' : undefined}>
                Command Center
              </button>
            </li>
          </ul>

          <div style={{ padding: '0 1rem', marginBottom: '0.5rem', fontSize: '0.75rem', fontWeight: 'bold', color: 'var(--text-muted)', letterSpacing: '1px' }}>AI OPERATIONS</div>
          <ul style={{ marginBottom: '2rem' }}>
            <li>
              <button className="nav-btn" onClick={() => setActiveTab('copilot')} aria-current={activeTab === 'copilot' ? 'page' : undefined}>
                Operations Copilot
              </button>
            </li>
            <li>
              <button className="nav-btn" onClick={() => setActiveTab('scenarios')} aria-current={activeTab === 'scenarios' ? 'page' : undefined}>
                What-If Simulator
              </button>
            </li>
            <li>
              <button className="nav-btn" onClick={() => setActiveTab('incidents')} aria-current={activeTab === 'incidents' ? 'page' : undefined}>
                Report Incident
              </button>
            </li>
          </ul>
          
        </nav>
        
        <main id="main-content" role="main" className="main-content" tabIndex={-1}>
          {activeTab === 'dashboard' && <Dashboard onNavigate={setActiveTab} />}
          {activeTab === 'copilot' && <CopilotForm />}
          {activeTab === 'scenarios' && <ScenarioForm />}
          {activeTab === 'incidents' && <IncidentForm />}
        </main>
      </div>
    </div>
  )
}

export default App
