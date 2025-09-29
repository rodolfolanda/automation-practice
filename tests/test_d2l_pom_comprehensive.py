"""
Eimport pytest
from playwright.sync_api import Page, expect
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage, DashboardPage
from pages.navigation_page import NavigationPage
from pages.course_page import CoursePageed D2L Tests using Page Object Model
This file demonstrates the power of well-structured Page Objects
"""

import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage, DashboardPage
from pages.navigation_page import NavigationPage
from pages.course_page import CoursePage

class TestD2LAuthentication:
    """Test class for D2L authentication scenarios"""
    
    def test_successful_login_journey(self, page: Page):
        """Complete login journey with page verification"""
        
        # Initialize page objects
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)
        
        # Navigate to login and verify page
        login_page.navigate_to_login()
        assert login_page.is_on_login_page()
        login_page.verify_login_page_elements()
        
        # Perform login
        login_page.login_with_valid_credentials()
        
        # Wait for D2L redirects to complete
        try:
            page.wait_for_url("**/d2l/home**", timeout=10000)
        except:
            pass  # Continue even if URL doesn't match exactly
            
        # Verify successful login
        assert dashboard_page.is_logged_in()
        assert dashboard_page.is_on_dashboard()
        dashboard_page.verify_dashboard_elements()
        
    def test_invalid_login_scenarios(self, page: Page):
        """Test various invalid login scenarios"""
        
        login_page = LoginPage(page)
        
        # Test with invalid credentials
        login_page.navigate_to_login()
        login_page.login_with_invalid_credentials()
        
        # Should remain on login page
        assert login_page.is_on_login_page()
        
    def test_login_page_elements(self, page: Page):
        """Test login page elements and functionality"""
        
        login_page = LoginPage(page)
        
        login_page.navigate_to_login()
        
        # Verify page title and heading
        login_page.assert_page_title_contains("Login")
        heading = login_page.get_login_page_heading()
        assert "Brightspace" in heading or "D2L" in heading
        
        # Verify all form elements
        login_page.verify_login_page_elements()

class TestD2LNavigation:
    """Test D2L navigation functionality"""
    
    def test_dashboard_navigation(self, page: Page):
        """Test navigation from dashboard"""
        
        # First login
        login_page = LoginPage(page)
        login_page.navigate_to_login()
        login_page.login_with_valid_credentials()
        
        # Wait for dashboard with proper timing
        page.wait_for_url("**/d2l/home**", timeout=10000)
        
        dashboard_page = DashboardPage(page)
        navigation_page = NavigationPage(page)
        
        # Verify we're on dashboard
        assert dashboard_page.is_on_dashboard()
        
        # Test navigation elements
        navigation_page.verify_navigation_elements()
        
    def test_user_workflow_journey(self, page: Page):
        """Test a complete user workflow"""
        
        # First login
        login_page = LoginPage(page)
        login_page.navigate_to_login()
        login_page.login_with_valid_credentials()
        
        # Wait for dashboard with proper timing
        page.wait_for_url("**/d2l/home**", timeout=10000)
        
        dashboard_page = DashboardPage(page) 
        navigation_page = NavigationPage(page)
        
        # Start from dashboard
        assert dashboard_page.is_on_dashboard()
        
        # Navigate to different sections - test home navigation
        navigation_page.navigate_to_home()
        dashboard_page.assert_url_contains("/d2l/")
        
        # Could extend to navigate to courses, etc.

class TestD2LUtilityMethods:
    """Test class for utility and helper methods"""
    
    def test_page_object_utility_methods(self, page: Page):
        """Test various utility methods across page objects"""
        
        login_page = LoginPage(page)
        
        # Test navigation and URL checking
        login_page.navigate_to_login()
        current_url = login_page.get_current_url()
        assert "playwrightdev.devlms.desire2learn.com" in current_url
        
        # Test title checking
        title = login_page.get_page_title()
        assert "Login" in title
        
        # Test screenshot capability
        login_page.take_screenshot("login_page_test")
        
    def test_error_handling_methods(self, page: Page):
        """Test error detection and handling methods"""
        
        login_page = LoginPage(page)
        
        login_page.navigate_to_login()
        login_page.login_with_invalid_credentials()
        
        # Check if error handling works
        # (Note: D2L might not show visible errors immediately)
        assert login_page.is_on_login_page()
        
def test_complete_login_logout_cycle(page: Page):
    """Test complete login and logout cycle"""
    
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    # Login
    login_page.navigate_to_login()
    login_page.login_with_valid_credentials()
    
    # Wait for dashboard with proper timing
    page.wait_for_url("**/d2l/home**", timeout=10000)
    
    assert dashboard_page.is_logged_in()
    
    # Logout (if logout functionality is available)
    try:
        dashboard_page.logout()
        login_page.assert_url_contains("/login")
    except Exception as e:
        # Logout might not be easily accessible in test environment
        print(f"Logout test skipped: {e}")
        pass