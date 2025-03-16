from typing import List, Optional
from datetime import datetime, timedelta

from .engine import session_scope
from .models import LLMCall


class LLMCallRepository:
    """Repository for LLM call logs."""

    @staticmethod
    def save(model_name: str, model_provider: str, prompt: str, response: Optional[str] = None, agent_name: Optional[str] = None, duration_ms: Optional[float] = None, success: bool = True, error_message: Optional[str] = None) -> LLMCall:
        """Save an LLM call log to the database."""
        with session_scope() as session:
            llm_call = LLMCall(model_name, model_provider, agent_name, prompt, response if response else None, duration_ms if duration_ms else None, success, error_message)
            session.add(llm_call)
            session.flush()  # Flush to get the ID
            session.refresh(llm_call)
            return llm_call

    @staticmethod
    def get_all() -> List[LLMCall]:
        """Get all LLM call logs."""
        with session_scope() as session:
            return session.query(LLMCall).all()

    @staticmethod
    def get_by_agent(agent_name: str) -> List[LLMCall]:
        """Get LLM call logs for a specific agent."""
        with session_scope() as session:
            return session.query(LLMCall).filter(LLMCall.agent_name == agent_name).all()

    @staticmethod
    def get_recent(days: int = 7) -> List[LLMCall]:
        """Get recent LLM call logs."""
        cutoff_date = datetime.utcnow() - timedelta(days=days)
        with session_scope() as session:
            return session.query(LLMCall).filter(LLMCall.timestamp >= cutoff_date).all()

    @staticmethod
    def get_failed() -> List[LLMCall]:
        """Get failed LLM call logs."""
        with session_scope() as session:
            return session.query(LLMCall).filter(LLMCall.success == False).all()
