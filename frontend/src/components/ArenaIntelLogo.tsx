import React from 'react';

interface Props {
  size?: number;
  monochrome?: boolean;
  className?: string;
}

export const ArenaIntelLogo: React.FC<Props> = ({ 
  size = 40, 
  monochrome = false, 
  className = '' 
}) => {
  const accentColor = monochrome ? 'currentColor' : 'var(--status-ai, #06b6d4)';
  const baseColor = 'currentColor';

  return (
    <svg 
      width={size} 
      height={size} 
      viewBox="0 0 100 100" 
      fill="none" 
      xmlns="http://www.w3.org/2000/svg"
      className={className}
      aria-hidden="true"
    >
      {/* Base field/arena */}
      <rect x="35" y="40" width="30" height="20" rx="4" stroke={baseColor} strokeWidth="4" fill="none" />
      
      {/* Stadium seating rings */}
      <path d="M20 50 C 20 25, 80 25, 80 50 C 80 75, 20 75, 20 50" stroke={baseColor} strokeWidth="4" fill="none" opacity="0.7" />
      <path d="M10 50 C 10 15, 90 15, 90 50 C 90 85, 10 85, 10 50" stroke={baseColor} strokeWidth="4" fill="none" strokeDasharray="8 6" opacity="0.4" />
      
      {/* AI Intelligence Node / Core */}
      <circle cx="50" cy="50" r="6" fill={accentColor} />
      
      {/* Uplink/Signal paths representing GenAI network */}
      <path d="M50 44 L50 32 M50 68 L50 56 M32 50 L20 50 M80 50 L68 50" stroke={accentColor} strokeWidth="3" strokeLinecap="round" />
    </svg>
  );
};
