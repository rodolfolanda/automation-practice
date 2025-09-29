"""
Base Page Object Class
This class contains common functionality that all page objects can inherit
"""

from playwright.sync_api import Page, expect
from typing import Optional
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from config import config

class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://practicetestautomation.com"  # Default base URL for practice sites
        
    def navigate_to(self, url: str):
        """Navigate to a specific URL"""
        self.page.goto(url)
        self.wait_for_page_load()
        
    def wait_for_page_load(self):
        """Wait for page to fully load"""
        self.page.wait_for_load_state("networkidle")
        
    def get_page_title(self) -> str:
        """Get the current page title"""
        return self.page.title()
        
    def get_current_url(self) -> str:
        """Get the current page URL"""
        return self.page.url
        
    def take_screenshot(self, name: str):
        """Take a screenshot with given name"""
        self.page.screenshot(path=f"screenshots/{name}.png")
        
    def wait_for_element(self, selector: str, timeout: int = 5000):
        """Wait for an element to be visible"""
        self.page.wait_for_selector(selector, timeout=timeout)
        
    def is_element_visible(self, selector: str) -> bool:
        """Check if an element is visible"""
        return self.page.locator(selector).is_visible()
        
    def get_element_text(self, selector: str) -> str:
        """Get text content of an element"""
        return self.page.locator(selector).text_content() or ""
        
    def click_element(self, selector: str):
        """Click an element with wait"""
        element = self.page.locator(selector)
        expect(element).to_be_visible()
        element.click()
        
    def fill_field(self, selector: str, value: str):
        """Fill a form field with wait"""
        element = self.page.locator(selector)
        expect(element).to_be_visible()
        element.fill(value)
        
    def wait_for_navigation(self):
        """Wait for navigation to complete"""
        self.page.wait_for_load_state("networkidle")
        
    def assert_url_contains(self, expected_path: str):
        """Assert that current URL contains expected path"""
        assert expected_path in self.get_current_url(), f"Expected URL to contain '{expected_path}', but got '{self.get_current_url()}'"
        
    def assert_url_not_contains(self, unexpected_path: str):
        """Assert that current URL does not contain unexpected path"""
        assert unexpected_path not in self.get_current_url(), f"Expected URL to NOT contain '{unexpected_path}', but got '{self.get_current_url()}'"
        
    def assert_page_title_contains(self, expected_title: str):
        """Assert that page title contains expected text"""
        title = self.get_page_title()
        assert expected_title in title, f"Expected title to contain '{expected_title}', but got '{title}'"