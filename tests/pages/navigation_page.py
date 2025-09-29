"""
Navigation Page Object for D2L
Handles common navigation elements and actions
"""

from playwright.sync_api import Page
from .base_page import BasePage

class NavigationPage(BasePage):
    """Page Object for D2L navigation elements"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        # D2L specific navigation selectors based on actual structure
        self.home_link = "a[aria-label='My Home']"  # Home link - will use .first in method
        self.quick_eval_link = "a.d2l-navigation-s-link:has-text('Quick Eval')"  # Specific Quick Eval link
        self.calendar_link = "a.d2l-navigation-s-link:has-text('Calendar')"  # Specific Calendar link  
        self.announcements_link = "a.d2l-navigation-s-link:has-text('Announcements')"  # Specific Announcements link
        self.navigation_container = "nav.d2l-navigation-s"  # Main navigation
        self.user_menu = "nav.d2l-navigation-s"  # User info in navigation
        self.notifications = "a:has-text('Announcements')"  # Notifications via announcements
        self.search_box = "input[placeholder*='search']"
        
    def navigate_to_home(self):
        """Navigate to home page"""
        # Use first instance if multiple elements match
        element = self.page.locator(self.home_link).first
        element.click()
        
    def navigate_to_quick_eval(self):
        """Navigate to Quick Eval page"""
        self.click_element(self.quick_eval_link)
        
    def navigate_to_calendar(self):
        """Navigate to calendar page"""
        self.click_element(self.calendar_link)
        
    def navigate_to_announcements(self):
        """Navigate to announcements page"""
        self.click_element(self.announcements_link)
        
    def open_user_menu(self):
        """Open the user dropdown menu"""
        self.click_element(self.user_menu)
        
    def search_for(self, search_term: str):
        """Search for content"""
        if self.is_element_visible(self.search_box):
            self.fill_field(self.search_box, search_term)
            self.page.keyboard.press("Enter")
        
    def check_notifications(self):
        """Click on notifications/announcements"""
        self.click_element(self.notifications)
        
    def verify_navigation_elements(self):
        """Verify main navigation elements are present"""
        assert self.is_element_visible(self.navigation_container), "Navigation container not visible"
        assert self.is_element_visible(self.quick_eval_link), "Quick Eval link not visible"
        assert self.is_element_visible(self.calendar_link), "Calendar link not visible"
        assert self.is_element_visible(self.announcements_link), "Announcements link not visible"
        
    def get_current_user_name(self):
        """Get the currently logged in user name from navigation"""
        nav_text = self.get_text(self.navigation_container)
        # Extract the first line which should be the username
        lines = nav_text.split('\n')
        return lines[0] if lines else "Unknown User"