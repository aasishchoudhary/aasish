from typing import Protocol

class ModelAdapter(Protocol):
    """Provider-neutral interface for a model integration."""
    def complete(self, prompt: str) -> str:
        ...
