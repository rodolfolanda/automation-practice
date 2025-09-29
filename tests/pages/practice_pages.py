"""
Page Objects for Practice Test Automation site
URL: https://practicetestautomation.com/practice/
"""
from tests.pages.base_page import BasePage


class PracticeLoginPage(BasePage):
    """Login page for Practice Test Automation site"""
    
    def __init__(self, page):
        super().__init__(page)
        self.base_url = "https://practicetestautomation.com"
        
        # Login page selectors
        self.username_input = "#username"
        self.password_input = "#password" 
        self.login_button = "#submit"
        self.success_message = ".post-title"
        self.error_message = "#error"
        self.logout_link = "text=Log out"
        
    def navigate_to_login(self):
        """Navigate to the practice login page"""
        login_url = f"{self.base_url}/practice-test-login/"
        self.navigate_to(login_url)
        self.assert_url_contains("practice-test-login")
        
    def login_with_credentials(self, username, password):
        """Perform login with given credentials"""
        self.fill_field(self.username_input, username)
        self.fill_field(self.password_input, password)
        self.click_element(self.login_button)
        
    def login_with_valid_credentials(self):
        """Login with known valid credentials for practice site"""
        self.login_with_credentials("student", "Password123")
        
    def login_with_invalid_credentials(self):
        """Login with invalid credentials for error testing"""
        self.login_with_credentials("incorrectUser", "Password123")
        
    def get_success_message(self):
        """Get the success message text after login"""
        return self.get_element_text(self.success_message)
        
    def get_error_message(self):
        """Get the error message text for failed login"""
        return self.get_element_text(self.error_message)
        
    def is_logged_in(self):
        """Check if user is successfully logged in"""
        return self.is_element_visible(self.success_message)
        
    def is_on_login_page(self):
        """Verify we are on the practice login page"""
        return "/practice-test-login" in self.get_current_url()
        
    def logout(self):
        """Logout from the application"""
        if self.is_element_visible(self.logout_link):
            self.click_element(self.logout_link)


class PracticeExceptionsPage(BasePage):
    """Exceptions page for practicing element interactions"""
    
    def __init__(self, page):
        super().__init__(page)
        self.base_url = "https://practicetestautomation.com"
        
        # Exception page selectors
        self.add_button = "#add_btn"
        self.delete_button = "#delete_btn" 
        self.row2_input = "input[id='row2']"
        self.confirmation_message = "#confirmation"
        
    def navigate_to_exceptions(self):
        """Navigate to the exceptions practice page"""
        exceptions_url = f"{self.base_url}/practice-test-exceptions/"
        self.navigate_to(exceptions_url)
        self.assert_url_contains("practice-test-exceptions")
        
    def click_add_button(self):
        """Click the Add button to add new row"""
        self.click_element(self.add_button)
        
    def wait_for_second_row(self, timeout=5000):
        """Wait for second row to appear"""
        self.page.wait_for_selector(self.row2_input, timeout=timeout)
        
    def enter_text_in_second_row(self, text):
        """Enter text in the second row input field"""
        self.fill_field(self.row2_input, text)
        
    def click_delete_button(self):
        """Click the Delete button"""
        self.click_element(self.delete_button)
        
    def wait_for_confirmation(self, timeout=5000):
        """Wait for confirmation message to appear"""
        self.page.wait_for_selector(self.confirmation_message, timeout=timeout)
        
    def get_confirmation_message(self):
        """Get the confirmation message text"""
        return self.get_element_text(self.confirmation_message)
        
    def is_second_row_visible(self):
        """Check if second row is visible"""
        return self.is_element_visible(self.row2_input)