from dataclasses import dataclass, field
from enum import Enum
from typing import Any

class ActionRisk(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

@dataclass(frozen=True)
class ActionRequest:
    name: str
    arguments: dict[str, Any] = field(default_factory=dict)
    risk: ActionRisk = ActionRisk.LOW

@dataclass(frozen=True)
class ExecutionEvent:
    event_type: str
    message: str
    metadata: dict[str, Any] = field(default_factory=dict)
