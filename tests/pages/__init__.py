"""
Page Objects Package for Practice Automation Tests

This package contains all Page Object Model classes for practice automation.

Available Page Objects:
- BasePage: Base class with common functionality
- PracticeLoginPage: Practice site login interactions
- PracticeExceptionsPage: Practice site exception handling
"""

from .base_page import BasePage
from .practice_pages import PracticeLoginPage, PracticeExceptionsPage

__all__ = [
    'BasePage',
    'PracticeLoginPage', 
    'PracticeExceptionsPage'
]