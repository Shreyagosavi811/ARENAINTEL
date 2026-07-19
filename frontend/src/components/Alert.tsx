import React from 'react';

interface Props {
  variant?: 'info' | 'warning' | 'danger' | 'success';
  icon?: React.ReactNode;
  children: React.ReactNode;
}

export const Alert: React.FC<Props> = ({ variant = 'info', icon, children }) => {
  return (
    <div className={`alert alert-${variant}`} role="alert" aria-live="polite">
      {icon && <span aria-hidden="true" style={{ fontSize: '1.2rem' }}>{icon}</span>}
      <div>{children}</div>
    </div>
  );
};
