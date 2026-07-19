import React from 'react';

interface Props {
  status: 'PENDING_REVIEW' | 'APPROVED' | 'REJECTED' | 'EXECUTED';
}

export const ApprovalStatusBadge: React.FC<Props> = ({ status }) => {
  let badgeClass = 'badge-medium';
  let label = 'Unknown';
  let icon = '';

  switch (status) {
    case 'PENDING_REVIEW':
      badgeClass = 'alert-warning';
      icon = '🤖';
      label = 'AI Generated (Pending Human Review)';
      break;
    case 'APPROVED':
      badgeClass = 'alert-success';
      icon = '✅';
      label = 'Human Approved (Ready to Execute)';
      break;
    case 'EXECUTED':
      badgeClass = 'alert-info';
      icon = '🚀';
      label = 'Executed in Field';
      break;
    case 'REJECTED':
      badgeClass = 'alert-danger';
      icon = '❌';
      label = 'Rejected by Human';
      break;
  }

  return (
    <div className={`badge ${badgeClass}`} role="status">
      <span aria-hidden="true" style={{ marginRight: '4px' }}>{icon}</span>
      {label}
    </div>
  );
};
