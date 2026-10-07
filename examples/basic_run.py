from core.models import ActionRequest, ActionRisk
from core.orchestrator import Orchestrator
from tools.calculator import Calculator

system = Orchestrator()
request = ActionRequest("calculate", {"left": 20, "operation": "*", "right": 5}, ActionRisk.LOW)
system.authorize(request)
print("Result:", Calculator().calculate(**request.arguments))
print("Evidence:")
for event in system.telemetry.snapshot():
    print(event)
