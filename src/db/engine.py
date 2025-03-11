import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager

from .models import Base

# Get database URL from environment variable or use a default SQLite database
DB_URL = os.environ.get("AIHF_DATABASE_URL", "sqlite:///ai_hedge_fund.db")

# Create engine and session factory
engine = create_engine(DB_URL)
SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)


def init_db():
    """Initialize the database, creating tables if they don't exist."""
    Base.metadata.create_all(engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
