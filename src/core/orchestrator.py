from core.models import ActionRequest, ExecutionEvent
from core.policy import Policy
from telemetry.events import EventLog

class Orchestrator:
    def __init__(self, policy: Policy | None = None, telemetry: EventLog | None = None):
        self.policy = policy or Policy()
        self.telemetry = telemetry or EventLog()

    def authorize(self, request: ActionRequest, approved: bool = False) -> None:
        self.policy.authorize(request, approved=approved)
        self.telemetry.record(ExecutionEvent("policy.authorized", request.name, {"risk": request.risk.value}))
