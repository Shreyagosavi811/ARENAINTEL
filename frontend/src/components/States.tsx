import React from 'react';

export const LoadingState: React.FC<{ message?: string }> = ({ message = "Processing..." }) => (
  <div className="card" style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-md)', color: 'var(--text-muted)' }} aria-live="polite">
    <span className="spinner"></span>
    <span>{message}</span>
  </div>
);

export const EmptyState: React.FC<{ message: string }> = ({ message }) => (
  <div className="card" style={{ textAlign: 'center', color: 'var(--text-muted)', fontStyle: 'italic' }}>
    {message}
  </div>
);

export const ErrorState: React.FC<{ error: any; onRetry: () => void }> = ({ error, onRetry }) => {
  let title = "Unexpected Server Error";
  let message = "An unknown error occurred while contacting the server.";
  
  if (error?.response) {
    const status = error.response.status;
    if (status === 401 || status === 403) {
      title = "Permission Failure";
      message = "You are not authorized to perform this operational action.";
    } else if (status === 503) {
      title = "AI Provider Unavailable";
      message = "The upstream intelligence service is currently offline. Please use standard manual SOPs.";
    } else if (status === 408 || status === 504) {
      title = "Timeout";
      message = "The AI analysis took too long to complete. The situation may be too complex, or the network is degraded.";
    } else if (status === 400) {
      title = "Validation Error";
      message = error.response.data?.detail || "Invalid input provided.";
    }
  } else if (error?.request) {
    title = "Network Error";
    message = "Connectivity lost. Please check your connection to the command center.";
  }

  return (
    <div className="alert alert-danger" style={{ flexDirection: 'column', gap: 'var(--space-md)' }} role="alert">
      <div>
        <h4 style={{ margin: '0 0 var(--space-sm) 0' }}>{title}</h4>
        <p style={{ margin: 0 }}>{message}</p>
      </div>
      <button className="btn btn-danger" onClick={onRetry} style={{ alignSelf: 'flex-start' }}>Retry Action</button>
    </div>
  );
};
