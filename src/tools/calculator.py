class Calculator:
    """Small deterministic example tool."""

    allowed_operations = {"+", "-", "*", "/"}

    def calculate(self, left: float, operation: str, right: float) -> float:
        if operation not in self.allowed_operations:
            raise ValueError(f"Unsupported operation: {operation}")
        if operation == "/" and right == 0:
            raise ValueError("Division by zero")
        return {"+": left + right, "-": left - right, "*": left * right, "/": left / right}[operation]
