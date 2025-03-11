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
        LLMCallRepository.save(model_name=model_name, model_provider=model_provider, prompt=str(prompt), response=str(response) if response else None, agent_name=agent_name, duration_ms=duration_ms, success=success, error_message=error_message)

    @staticmethod
    def timed_call(call_function, prompt: Any, model_name: str, model_provider: str, pydantic_model: Type[T], agent_name: Optional[str] = None, **kwargs) -> T:
        """
        Execute an LLM call and log it with timing.

        Args:
            call_function: The function to call the LLM
            prompt: The prompt to send to the LLM
            model_name: Name of the model to use
            model_provider: Provider of the model
            pydantic_model: The Pydantic model class to structure the output
            agent_name: Optional name of the agent for progress updates
            **kwargs: Additional keyword arguments for the call function

        Returns:
            An instance of the specified Pydantic model
        """
        start_time = time.time()
        success = True
        error_msg = None
        result = None

        try:
            result = call_function(prompt=prompt, model_name=model_name, model_provider=model_provider, pydantic_model=pydantic_model, agent_name=agent_name, **kwargs)
            return result
        except Exception as e:
            success = False
            error_msg = str(e)
            raise
        finally:
            end_time = time.time()
            duration_ms = (end_time - start_time) * 1000

            # Log the call
            LLMLogger.log_call(prompt=prompt, model_name=model_name, model_provider=model_provider, response=result, agent_name=agent_name, duration_ms=duration_ms, success=success, error_message=error_msg)
