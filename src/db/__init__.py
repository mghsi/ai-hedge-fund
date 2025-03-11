from .engine import init_db, session_scope
from .logger import LLMLogger
from .models import LLMCall
from .repository import LLMCallRepository

# Initialize database when the package is imported
init_db()

__all__ = ["LLMLogger", "LLMCall", "LLMCallRepository", "init_db", "session_scope"]
