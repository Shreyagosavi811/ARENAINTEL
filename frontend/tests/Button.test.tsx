import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import { Button } from "../src/components/Button";

describe("Button component", () => {
  it("renders correctly with children", () => {
    render(<Button>Click Me</Button>);
    expect(screen.getByText("Click Me")).toBeDefined();
  });

  it("calls onClick handler", () => {
    const handleClick = vi.fn();
    render(<Button onClick={handleClick}>Action</Button>);
    fireEvent.click(screen.getByText("Action"));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
});
