import pytest
from core.models import ActionRequest, ActionRisk
from core.policy import Policy, PolicyError

def test_low_risk_action_is_allowed():
    Policy().authorize(ActionRequest("read_status", risk=ActionRisk.LOW))

def test_high_risk_requires_approval():
    with pytest.raises(PolicyError):
        Policy().authorize(ActionRequest("delete_resource", risk=ActionRisk.HIGH))

def test_high_risk_can_be_approved():
    Policy().authorize(ActionRequest("delete_resource", risk=ActionRisk.HIGH), approved=True)
