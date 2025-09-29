"""
Page Object Model for Login Page
This represents the login page and its interactions
"""

from playwright.sync_api import Page, expect
from .base_page import BasePage
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from config import config

class LoginPage(BasePage):
    """Page Object for the login page"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Selectors - D2L login page specific
        self.username_input = "#userName"
        self.password_input = "input[type='password']"
        self.login_button = "button.d2l-button:has-text('Log In')"
        self.error_message = ".d2l-error, .error, [role='alert']"
        self.forgot_password_link = "a:has-text('Forgot your password?')"
        self.login_form = "form"
        self.page_heading = ".d2l-login-portal-heading"
        
    def navigate_to_login(self):
        """Navigate to the login page"""
        self.page.goto(config.get_login_url())  # Direct navigation to login URL
        self.wait_for_page_load()
        
    def enter_username(self, username: str):
        """Enter username in the username field"""
        self.fill_field(self.username_input, username)
        
    def enter_password(self, password: str):
        """Enter password in the password field"""
        self.fill_field(self.password_input, password)
        
    def click_login(self):
        """Click the login button"""
        self.click_element(self.login_button)
        self.wait_for_navigation()
        
    def login(self, username: str, password: str):
        """Complete login process with username and password"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
    def login_with_valid_credentials(self):
        """Login with credentials from environment variables"""
        username, password = config.get_d2l_credentials()
        self.login(username, password)
        
    def login_with_invalid_credentials(self):
        """Login with invalid credentials for testing"""
        self.login("invalid_user", "wrong_password")
        
    def get_error_message(self):
        """Get the error message text"""
        return self.get_element_text(self.error_message)
        
    def is_error_visible(self):
        """Check if error message is visible"""
        return self.is_element_visible(self.error_message)
        
    def is_on_login_page(self) -> bool:
        """Verify we are on the login page"""
        return "/d2l/login" in self.get_current_url()
        
    def click_forgot_password(self):
        """Click the forgot password link"""
        self.click_element(self.forgot_password_link)
        
    def get_login_page_heading(self) -> str:
        """Get the main heading text on login page"""
        return self.get_element_text(self.page_heading)
        
    def verify_login_page_elements(self):
        """Verify all expected elements are present on login page"""
        assert self.is_element_visible(self.username_input), "Username field not visible"
        assert self.is_element_visible(self.password_input), "Password field not visible"  
        assert self.is_element_visible(self.login_button), "Login button not visible"
        assert self.is_element_visible(self.forgot_password_link), "Forgot password link not visible"

class DashboardPage(BasePage):
    """Page Object for the D2L dashboard/home page"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        # D2L Dashboard specific selectors
        self.user_menu = "d2l-dropdown-menu[text*='User']"
        self.logout_button = "d2l-menu-item:has-text('Logout')"
        self.navigation_bar = ".d2l-navigation-s"
        self.main_content = ".d2l-page-main"
        self.course_tiles = ".d2l-widget"
        
    def is_logged_in(self) -> bool:
        """Check if user is successfully logged in to D2L"""
        return ("/d2l/home" in self.get_current_url() and 
                self.is_element_visible(self.navigation_bar))
        
    def is_on_dashboard(self) -> bool:
        """Verify we are on the dashboard page"""
        return "/d2l/home" in self.get_current_url()
        
    def get_dashboard_title(self) -> str:
        """Get the dashboard page title"""
        return self.get_page_title()
        
    def logout(self):
        """Logout from D2L"""
        if self.is_element_visible(self.user_menu):
            self.click_element(self.user_menu)
            self.click_element(self.logout_button)
        else:
            # Alternative logout method if user menu is different
            print("User menu not found, looking for alternative logout method")
            
    def verify_dashboard_elements(self):
        """Verify expected dashboard elements are present"""
        assert self.is_element_visible(self.navigation_bar), "Navigation bar not visible"
        assert self.is_element_visible(self.main_content), "Main content area not visible"
        
    def navigate_to_courses(self):
        """Navigate to courses section"""
        # This would be implemented based on D2L navigation structure
        pass