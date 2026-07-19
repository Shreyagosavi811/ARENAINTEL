import React, { useState } from 'react';
import { ConfirmDialog } from '../../../components/ConfirmDialog';

interface Props {
  canApprove: boolean;
  onStatusChange?: (status: 'APPROVED' | 'REJECTED') => void;
}

export const ApprovalPanel: React.FC<Props> = ({ canApprove, onStatusChange }) => {
  const [status, setStatus] = useState<'PENDING_REVIEW' | 'APPROVED' | 'REJECTED'>('PENDING_REVIEW');
  const [isDialogOpem, setIsDialogOpen] = useState(false);
  const [pendingAction, setPendingAction] = useState<'APPROVE' | 'REJECT' | null>(null);

  const handleConfirm = () => {
    setIsDialogOpen(false);
    if (pendingAction === 'APPROVE') setStatus('APPROVED');
    if (pendingAction === 'REJECT') setStatus('REJECTED');
    if (onStatusChange && pendingAction) onStatusChange(pendingAction === 'APPROVE' ? 'APPROVED' : 'REJECTED');
    setPendingAction(null);
  };

  if (!canApprove) return null;

  return (
    <div className="human-boundary" aria-labelledby="approval-heading">
      <h3 id="approval-heading" style={{ margin: '0 0 var(--space-sm) 0', color: 'var(--text-primary)' }}>🧑‍⚖️ Human Authorization Required</h3>
      <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginBottom: 'var(--space-md)' }}>
        AI generated this recommendation. Approval authorizes operational deployment but does not execute it automatically.
      </p>

      {status === 'PENDING_REVIEW' ? (
        <div style={{ display: 'flex', gap: 'var(--space-md)' }}>
          <button className="btn btn-success" onClick={() => { setPendingAction('APPROVE'); setIsDialogOpen(true); }}>
            Authorize Plan
          </button>
          <button className="btn btn-danger" onClick={() => { setPendingAction('REJECT'); setIsDialogOpen(true); }}>
            Reject Plan
          </button>
        </div>
      ) : (
        <div style={{ padding: 'var(--space-md)', background: 'var(--bg-app)', borderRadius: 'var(--radius-md)', borderLeft: `4px solid ${status === 'APPROVED' ? 'var(--status-nominal)' : 'var(--status-critical)'}` }}>
          <strong>AUDIT TRAIL: </strong> 
          Plan was {status} by current user. State is locked.
        </div>
      )}

      <ConfirmDialog 
        isOpen={isDialogOpem}
        title={pendingAction === 'APPROVE' ? 'Authorize Operational Plan?' : 'Reject Operational Plan?'}
        message={pendingAction === 'APPROVE' ? 'Are you sure you want to authorize these actions? This will transition the plan to an APPROVED state.' : 'Are you sure you want to discard this AI recommendation?'}
        confirmText={pendingAction === 'APPROVE' ? 'Yes, Authorize' : 'Yes, Reject'}
        isDestructive={pendingAction === 'REJECT'}
        onConfirm={handleConfirm}
        onCancel={() => { setIsDialogOpen(false); setPendingAction(null); }}
      />
    </div>
  );
};
