import pytest
from src.agents.ben_graham import ben_graham_agent
from src.agents.warren_buffett import warren_buffett_agent
from src.agents.charlie_munger import charlie_munger_agent
from src.agents.bill_ackman import bill_ackman_agent
from src.agents.cathie_wood import cathie_wood_agent
from src.agents.stanley_druckenmiller import stanley_druckenmiller_agent
from src.agents.fundamentals import fundamentals_agent
from src.agents.sentiment import sentiment_agent
from src.agents.technicals import technical_analyst_agent
from src.agents.valuation import valuation_agent


@pytest.fixture
def analyst_functions_map():
    """Return a mapping of analyst keys to their agent functions."""
    return {"ben_graham": ben_graham_agent, "bill_ackman": bill_ackman_agent, "cathie_wood": cathie_wood_agent, "charlie_munger": charlie_munger_agent, "stanley_druckenmiller": stanley_druckenmiller_agent, "warren_buffett": warren_buffett_agent, "technical_analyst": technical_analyst_agent, "fundamentals_analyst": fundamentals_agent, "sentiment_analyst": sentiment_agent, "valuation_analyst": valuation_agent}


@pytest.fixture
def analyst_display_names():
    """Return a mapping of analyst keys to their display names."""
    return {"ben_graham": "Ben Graham", "bill_ackman": "Bill Ackman", "cathie_wood": "Cathie Wood", "charlie_munger": "Charlie Munger", "stanley_druckenmiller": "Stanley Druckenmiller", "warren_buffett": "Warren Buffett", "technical_analyst": "Technical Analyst", "fundamentals_analyst": "Fundamentals Analyst", "sentiment_analyst": "Sentiment Analyst", "valuation_analyst": "Valuation Analyst"}


@pytest.fixture
def analyst_orders():
    """Return a mapping of analyst keys to their expected order."""
    return {"ben_graham": 0, "bill_ackman": 1, "cathie_wood": 2, "charlie_munger": 3, "stanley_druckenmiller": 4, "warren_buffett": 5, "technical_analyst": 6, "fundamentals_analyst": 7, "sentiment_analyst": 8, "valuation_analyst": 9}
