import React, { useEffect, useRef } from 'react';

interface Props {
  isOpen: boolean;
  title: string;
  message: string;
  confirmText?: string;
  cancelText?: string;
  isDestructive?: boolean;
  onConfirm: () => void;
  onCancel: () => void;
}

export const ConfirmDialog: React.FC<Props> = ({ isOpen, title, message, confirmText = 'Confirm', cancelText = 'Cancel', isDestructive = false, onConfirm, onCancel }) => {
  const dialogRef = useRef<HTMLDialogElement>(null);
  const previousFocusRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    const dialog = dialogRef.current;
    if (isOpen && dialog && !dialog.open) {
      previousFocusRef.current = document.activeElement as HTMLElement;
      dialog.showModal();
    } else if (!isOpen && dialog && dialog.open) {
      dialog.close();
      if (previousFocusRef.current) {
        previousFocusRef.current.focus();
      }
    }
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div className="dialog-backdrop">
      <dialog 
        ref={dialogRef} 
        className="dialog-content" 
        onCancel={onCancel}
        aria-labelledby="dialog-title"
        aria-describedby="dialog-desc"
      >
        <h3 id="dialog-title" style={{ margin: '0 0 var(--space-sm) 0', fontSize: '1.25rem' }}>{title}</h3>
        <p id="dialog-desc" style={{ color: 'var(--text-muted)' }}>{message}</p>
        <div className="dialog-footer">
          <button className="btn" onClick={onCancel}>{cancelText}</button>
          <button className={`btn ${isDestructive ? 'btn-danger' : 'btn-success'}`} onClick={onConfirm}>
            {confirmText}
          </button>
        </div>
      </dialog>
    </div>
  );
};
