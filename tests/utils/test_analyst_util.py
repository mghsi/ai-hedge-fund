import pytest
from src.utils.analysts import ANALYST_CONFIG, ANALYST_ORDER, get_analyst_nodes
from src.agents.ben_graham import ben_graham_agent
from src.agents.charlie_munger import charlie_munger_agent
from src.agents.warren_buffett import warren_buffett_agent
from src.agents.bill_ackman import bill_ackman_agent
from src.agents.cathie_wood import cathie_wood_agent
from src.agents.stanley_druckenmiller import stanley_druckenmiller_agent
from src.agents.fundamentals import fundamentals_agent
from src.agents.sentiment import sentiment_agent
from src.agents.technicals import technical_analyst_agent
from src.agents.valuation import valuation_agent
from tests.fixtures.analyst_fixtures import analyst_functions_map, analyst_display_names, analyst_orders


class TestAnalystConfig:
    def test_analyst_config_structure(self):
        """Test that ANALYST_CONFIG has the expected structure and entries."""
        required_keys = ["ben_graham", "bill_ackman", "cathie_wood", "charlie_munger", "stanley_druckenmiller", "warren_buffett", "technical_analyst", "fundamentals_analyst", "sentiment_analyst", "valuation_analyst"]

        for key in required_keys:
            assert key in ANALYST_CONFIG

        for key, config in ANALYST_CONFIG.items():
            assert "display_name" in config
            assert "agent_func" in config
            assert "order" in config
            assert isinstance(config["display_name"], str)
            assert callable(config["agent_func"])
            assert isinstance(config["order"], int)

    @pytest.mark.parametrize("key", ["ben_graham", "bill_ackman", "cathie_wood", "charlie_munger", "stanley_druckenmiller", "warren_buffett", "technical_analyst", "fundamentals_analyst", "sentiment_analyst", "valuation_analyst"])
    def test_analyst_config_entries(self, key, analyst_display_names, analyst_functions_map, analyst_orders):
        """Test each analyst configuration entry."""
        assert key in ANALYST_CONFIG
        assert ANALYST_CONFIG[key]["display_name"] == analyst_display_names[key]
        assert ANALYST_CONFIG[key]["agent_func"] == analyst_functions_map[key]
        assert ANALYST_CONFIG[key]["order"] == analyst_orders[key]

    def test_analyst_order_derivation(self):
        """Test that ANALYST_ORDER is correctly derived from ANALYST_CONFIG."""
        # Sort the config by order as done in the implementation
        sorted_config = sorted(ANALYST_CONFIG.items(), key=lambda x: x[1]["order"])
        expected_order = [(config["display_name"], key) for key, config in sorted_config]

        assert ANALYST_ORDER == expected_order

        # Check first and last entries explicitly
        assert ANALYST_ORDER[0] == ("Ben Graham", "ben_graham")
        assert ANALYST_ORDER[-1] == ("Valuation Analyst", "valuation_analyst")

    def test_get_analyst_nodes(self):
        """Test that get_analyst_nodes returns the expected mapping."""
        nodes = get_analyst_nodes()

        # Check the structure of the returned nodes
        assert len(nodes) == len(ANALYST_CONFIG)

        # Check specific entries
        assert nodes["ben_graham"] == ("ben_graham_agent", ben_graham_agent)
        assert nodes["warren_buffett"] == ("warren_buffett_agent", warren_buffett_agent)

        # Check that all entries follow the expected pattern
        for key, config in ANALYST_CONFIG.items():
            expected_node = (f"{key}_agent", config["agent_func"])
            assert nodes[key] == expected_node

    def test_analyst_config_completeness(self, analyst_functions_map):
        """Test that all required agent functions exist and are correctly mapped."""
        for key, expected_func in analyst_functions_map.items():
            assert key in ANALYST_CONFIG
            assert ANALYST_CONFIG[key]["agent_func"] == expected_func
