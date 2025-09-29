"""
Login Tests using Page Object Model
This demonstrates best practices for organizing test code
"""

import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage, DashboardPage
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import config

def test_successful_login_with_pom(page: Page):
    """Test successful login using Page Object Model"""
    
    # Initialize page objects
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    # Test steps using page object methods
    login_page.navigate_to_login()
    login_page.login_with_valid_credentials()  # Now uses environment variables
    
    # Wait for D2L's specific redirect pattern (same as comprehensive tests)
    page.wait_for_url("**/d2l/home**", timeout=10000)
    
    # Verify login success
    assert dashboard_page.is_logged_in()
    assert "/d2l/home" in page.url
    
def test_invalid_login_with_pom(page: Page):
    """Test invalid login using Page Object Model"""
    
    login_page = LoginPage(page)
    
    login_page.navigate_to_login()
    login_page.login("wronguser", "wrongpass")
    
    # Verify we're still on login page (login failed)
    assert "/d2l/login" in page.url, "Should still be on login page after invalid login"
    
def test_step_by_step_login_with_pom(page: Page):
    """Test your exact 4 steps using Page Object Model"""
    
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    # Step 1: Open URL
    login_page.navigate_to_login()
    
    # Step 2: Enter userid  
    username, password = config.get_d2l_credentials()
    login_page.enter_username(username)
    
    # Step 3: Enter password
    login_page.enter_password(password)
    
    # Step 4: Click login
    login_page.click_login()
    
    # Verify success - wait for D2L's specific redirect pattern
    page.wait_for_url("**/d2l/home**", timeout=10000)
    assert "/d2l/home" in page.url, "Should be redirected to D2L home after successful login"