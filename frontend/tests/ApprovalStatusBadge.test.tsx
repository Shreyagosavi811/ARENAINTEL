import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import { ApprovalStatusBadge } from "../src/features/approvals/components/ApprovalStatusBadge";

describe("ApprovalStatusBadge component", () => {
  it("renders pending review explicitly as AI generated", () => {
    render(<ApprovalStatusBadge status="PENDING_REVIEW" />);
    expect(screen.getByText(/AI Generated/i)).toBeDefined();
  });

  it("renders approved explicitly as Human Approved", () => {
    render(<ApprovalStatusBadge status="APPROVED" />);
    expect(screen.getByText(/Human Approved/i)).toBeDefined();
  });
  
  it("renders executed explicitly", () => {
    render(<ApprovalStatusBadge status="EXECUTED" />);
    expect(screen.getByText(/Executed in Field/i)).toBeDefined();
  });
});
