from core.models import ActionRequest, ActionRisk
from core.orchestrator import Orchestrator

def test_authorized_event_is_recorded():
    system = Orchestrator()
    system.authorize(ActionRequest("read_status", risk=ActionRisk.LOW))
    events = system.telemetry.snapshot()
    assert len(events) == 1
    assert events[0]["event_type"] == "policy.authorized"
    assert events[0]["metadata"]["risk"] == "low"
