import React from "react";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "danger";
  children: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({ variant = "primary", children, ...props }) => {
  const baseClass = "btn";
  const variantClass = `btn-${variant}`;
  
  return (
    <button className={`${baseClass} ${variantClass}`} {...props}>
      {children}
    </button>
  );
};
