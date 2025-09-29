"""
Page Objects Package for D2L Playwright Tests

This package contains all Page Object Model classes for D2L testing.

Available Page Objects:
- BasePage: Base class with common functionality
- LoginPage: Login page interactions
- DashboardPage: Dashboard/home page interactions  
- NavigationPage: Navigation elements and actions
- CoursePage: Course-specific functionality
"""

from .base_page import BasePage
from .login_page import LoginPage, DashboardPage
from .navigation_page import NavigationPage
from .course_page import CoursePage

__all__ = [
    'BasePage',
    'LoginPage', 
    'DashboardPage',
    'NavigationPage',
    'CoursePage'
]