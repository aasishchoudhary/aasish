from .models import ActionRequest, ActionRisk

class PolicyError(PermissionError):
    """Raised when an action violates execution policy."""

class Policy:
    def __init__(self, require_approval_for: set[ActionRisk] | None = None):
        self.require_approval_for = require_approval_for or {ActionRisk.HIGH, ActionRisk.MEDIUM}

    def authorize(self, request: ActionRequest, approved: bool = False) -> None:
        if request.risk in self.require_approval_for and not approved:
            raise PolicyError(f"Explicit approval required for {request.risk.value}-risk action: {request.name}")
