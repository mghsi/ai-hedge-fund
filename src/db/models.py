from sqlalchemy import Column, Integer, String, Float, Text, Boolean, DateTime
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()


class LLMCall(Base):
    """Model for logging LLM calls."""

    __tablename__ = "llm_calls"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    model_name = Column(String(100), nullable=False)
    model_provider = Column(String(100), nullable=False)
    agent_name = Column(String(100), nullable=True)
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=True)
    duration_ms = Column(Float, nullable=True)
    success = Column(Boolean, default=True)
    error_message = Column(Text, nullable=True)

    def __repr__(self):
        return f"<LLMCall(id={self.id}, timestamp={self.timestamp}, " f"model={self.model_name}, provider={self.model_provider}, " f"agent={self.agent_name}, success={self.success})>"
