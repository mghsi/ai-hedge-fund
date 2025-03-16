import time
from typing import Any, Optional, Type, TypeVar
from pydantic import BaseModel

from .repository import LLMCallRepository

T = TypeVar("T", bound=BaseModel)


class LLMLogger:
    """Logger for LLM calls."""

    @staticmethod
    def log_call(prompt: Any, model_name: str, model_provider: str, response: Any = None, agent_name: Optional[str] = None, duration_ms: Optional[float] = None, success: bool = True, error_message: Optional[str] = None) -> None:
        """Log an LLM call."""
        LLMCallRepository.save(model_name, model_provider, prompt=str(prompt), response=str(response) if response else None, agent_name=agent_name, duration_ms=duration_ms, success=success, error_message=error_message)
