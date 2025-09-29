"""
Practice site test suite for learning Playwright automation
Uses https://practicetestautomation.com/practice/ - safe for learning
"""
import pytest
from playwright.sync_api import Page
from tests.pages.practice_pages import PracticeLoginPage, PracticeExceptionsPage


class TestPracticeLogin:
    """Test suite for practice login scenarios"""
    
    def test_successful_login(self, page: Page):
        """Practice: Successful login with valid credentials"""
        login_page = PracticeLoginPage(page)
        
        # Navigate and login
        login_page.navigate_to_login()
        login_page.login_with_valid_credentials()
        
        # Verify success
        assert login_page.is_logged_in()
        success_message = login_page.get_success_message()
        assert "Logged In Successfully" in success_message
        
    def test_invalid_username_login(self, page: Page):
        """Practice: Login with invalid username"""
        login_page = PracticeLoginPage(page)
        
        # Navigate and attempt invalid login
        login_page.navigate_to_login()
        login_page.login_with_invalid_credentials()
        
        # Verify error
        error_message = login_page.get_error_message()
        assert "Your username is invalid!" in error_message
        
    def test_invalid_password_login(self, page: Page):
        """Practice: Login with invalid password"""
        login_page = PracticeLoginPage(page)
        
        # Navigate and login with wrong password
        login_page.navigate_to_login()
        login_page.login_with_credentials("student", "wrongPassword")
        
        # Verify error
        error_message = login_page.get_error_message()
        assert "Your password is invalid!" in error_message
        
    def test_step_by_step_login(self, page: Page):
        """Practice: Step-by-step login process"""
        login_page = PracticeLoginPage(page)
        
        # Step 1: Navigate
        login_page.navigate_to_login()
        assert login_page.is_on_login_page()
        
        # Step 2: Fill username
        login_page.fill_field(login_page.username_input, "student")
        
        # Step 3: Fill password  
        login_page.fill_field(login_page.password_input, "Password123")
        
        # Step 4: Click login
        login_page.click_element(login_page.login_button)
        
        # Step 5: Verify success
        assert login_page.is_logged_in()


class TestPracticeExceptions:
    """Test suite for practicing dynamic elements and exceptions"""
    
    def test_add_new_element(self, page: Page):
        """Practice: Add new element dynamically"""
        exceptions_page = PracticeExceptionsPage(page)
        
        # Navigate to exceptions page
        exceptions_page.navigate_to_exceptions()
        
        # Initially second row should not exist
        assert not exceptions_page.is_second_row_visible()
        
        # Click Add button
        exceptions_page.click_add_button()
        
        # Wait for new row to appear
        exceptions_page.wait_for_second_row()
        
        # Verify second row is now visible
        assert exceptions_page.is_second_row_visible()
        
    def test_add_and_delete_element(self, page: Page):
        """Practice: Add element then delete it"""
        exceptions_page = PracticeExceptionsPage(page)
        
        # Navigate and add element
        exceptions_page.navigate_to_exceptions()
        exceptions_page.click_add_button()
        exceptions_page.wait_for_second_row()
        
        # Enter text in new row
        exceptions_page.enter_text_in_second_row("Practice Text")
        
        # Remove the row
        exceptions_page.click_remove_button()
        
        # Wait for confirmation
        exceptions_page.wait_for_confirmation()
        
        # Verify confirmation message
        confirmation = exceptions_page.get_confirmation_message()
        assert "Row 2 was removed" in confirmation
        
    def test_exception_handling_no_such_element(self, page: Page):
        """Practice: Handle NoSuchElementException"""
        exceptions_page = PracticeExceptionsPage(page)
        
        # Navigate to page
        exceptions_page.navigate_to_exceptions()
        
        # Try to interact with element that doesn't exist yet
        # This should be handled gracefully
        assert not exceptions_page.is_second_row_visible()
        
        # Add the element first
        exceptions_page.click_add_button()
        exceptions_page.wait_for_second_row()
        
        # Now it should be visible
        assert exceptions_page.is_second_row_visible()


@pytest.mark.skip(reason="Enable these for additional practice sites")
class TestOtherPracticeSites:
    """Additional practice with other safe automation sites"""
    
    def test_the_internet_login(self, page: Page):
        """Practice with The Internet Heroku app"""
        page.goto("https://the-internet.herokuapp.com/login")
        
        # Valid login
        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        page.click("button[type='submit']")
        
        # Verify success
        success_message = page.locator(".flash.success")
        assert success_message.is_visible()
        assert "You logged into a secure area!" in success_message.text_content()
        
    def test_sauce_demo_workflow(self, page: Page):
        """Practice with Sauce Demo e-commerce site"""
        page.goto("https://www.saucedemo.com/")
        
        # Login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce") 
        page.click("#login-button")
        
        # Add item to cart
        page.click("[data-test='add-to-cart-sauce-labs-backpack']")
        
        # Verify item added
        cart_badge = page.locator(".shopping_cart_badge")
        assert cart_badge.text_content() == "1"