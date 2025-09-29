"""
pytest configuration for Playwright tests
"""

import pytest
from playwright.sync_api import Playwright, Browser

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context for all tests"""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True
    }

@pytest.fixture(scope="session") 
def browser_type_launch_args(browser_type_launch_args):
    """Configure browser launch arguments"""
    return {
        **browser_type_launch_args,
        # Don't override headless here - let command line flags control it
        "slow_mo": 100      # Slow down by 100ms per action for demo purposes
    }