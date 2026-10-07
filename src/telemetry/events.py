from dataclasses import asdict
from datetime import datetime, timezone
from typing import Any
from core.models import ExecutionEvent

class EventLog:
    def __init__(self):
        self.events: list[dict[str, Any]] = []

    def record(self, event: ExecutionEvent) -> None:
        item = asdict(event)
        item["timestamp"] = datetime.now(timezone.utc).isoformat()
        self.events.append(item)

    def snapshot(self) -> list[dict[str, Any]]:
        return list(self.events)
