"""
Configuration module for Practice Playwright automation
Simple configuration for practice websites - no sensitive credentials needed!
"""

import os
from dotenv import load_dotenv
from pathlib import Path

class Config:
    """Configuration class for practice automation"""
    
    def __init__(self):
        # Load environment variables from .env file (optional for practice)
        env_path = Path(__file__).parent / '.env'
        if env_path.exists():
            load_dotenv(dotenv_path=env_path)
        
        # Practice Site URLs (public sites, no credentials needed)
        self.PRACTICE_LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"
        self.PRACTICE_EXCEPTIONS_URL = "https://practicetestautomation.com/practice-test-exceptions/"
        self.THE_INTERNET_URL = "https://the-internet.herokuapp.com/"
        self.SAUCE_DEMO_URL = "https://www.saucedemo.com/"
        self.PLAYWRIGHT_DEMO_URL = "https://demo.playwright.dev/"
        
        # Test Configuration
        self.DEFAULT_TIMEOUT = int(os.getenv('DEFAULT_TIMEOUT', '10000'))
        self.HEADLESS_MODE = os.getenv('HEADLESS_MODE', 'false').lower() == 'true'
        
        # Practice site credentials (public knowledge - no security risk)
        self.PRACTICE_CREDENTIALS = {
            'valid_username': 'student',
            'valid_password': 'Password123',
            'invalid_username': 'incorrectUser',
            'invalid_password': 'wrongPassword'
        }
        
        self.SAUCE_DEMO_CREDENTIALS = {
            'standard_user': 'secret_sauce',
            'locked_out_user': 'secret_sauce',
            'problem_user': 'secret_sauce'
        }
        
        self.THE_INTERNET_CREDENTIALS = {
            'username': 'tomsmith',
            'password': 'SuperSecretPassword!'
        }
    
    def get_practice_credentials(self, credential_type='valid'):
        """Get practice site credentials"""
        if credential_type == 'valid':
            return (self.PRACTICE_CREDENTIALS['valid_username'], 
                   self.PRACTICE_CREDENTIALS['valid_password'])
        elif credential_type == 'invalid':
            return (self.PRACTICE_CREDENTIALS['invalid_username'],
                   self.PRACTICE_CREDENTIALS['valid_password'])
        else:
            raise ValueError(f"Unknown credential type: {credential_type}")
    
    def get_sauce_demo_credentials(self, user_type='standard_user'):
        """Get Sauce Demo credentials"""
        return (user_type, self.SAUCE_DEMO_CREDENTIALS[user_type])
    
    def get_the_internet_credentials(self):
        """Get The Internet credentials"""
        return (self.THE_INTERNET_CREDENTIALS['username'],
               self.THE_INTERNET_CREDENTIALS['password'])

# Global config instance
config = Config()