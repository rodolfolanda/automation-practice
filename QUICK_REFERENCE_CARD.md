# 🚀 Playwright Practice Automation - Quick Command Reference Card

## 📂 Daily Startup
```bash
cd ~/automation-practice/playwright-practice-automation

# 🚀 EASIEST: Use the convenience script (recommended)
./run_tests.sh

# Manual way:
source venv/bin/activate
```

## 🧪 Essential Test Commands

### 🚀 **EASY WAY (Recommended)**
```bash
# Run all tests
./run_tests.sh

# Run specific test file
./run_tests.sh tests/test_practice_sites.py -v --headed

# Run specific test  
./run_tests.sh tests/test_practice_sites.py::TestPracticeLogin::test_successful_login -v --headed

# Debug mode (slow + visible)
./run_tests.sh tests/test_practice_sites.py -v -s --headed --slowmo=1000
```

### 📋 **Manual Way (if needed)**
```bash
# Requires setting PYTHONPATH manually
PYTHONPATH=/Users/rlanda/automation-practice/playwright-practice-automation/tests pytest tests/test_practice_sites.py -v --headed
```

## 🌐 Browser Commands
```bash
# 🚀 Easy way - Different browsers  
./run_tests.sh tests/test_practice_sites.py --browser chromium --headed  # Chrome
./run_tests.sh tests/test_practice_sites.py --browser firefox --headed   # Firefox
./run_tests.sh tests/test_practice_sites.py --browser webkit --headed    # Safari-like

# Update browsers
playwright install
```

## 📋 Your Current Test Files
```bash
# Practice site login tests
pytest tests/test_practice_sites.py::TestPracticeLogin -v --headed

# Practice site exception handling tests
pytest tests/test_practice_sites.py::TestPracticeExceptions -v --headed

# Demo site tests
pytest tests/test_demo_practice.py::TestPlaywrightDemo -v --headed
```

## 🔧 Debug Commands
```bash
# See failures only
pytest --lf -v --headed

# Stop at first failure  
pytest -x -v --headed

# Full error details
pytest --tb=long
```

## 📁 Project Structure
```
tests/
├── pages/
│   ├── base_page.py        # Foundation (inherit from this)
│   ├── practice_pages.py   # Practice site page objects
│   └── demo_page.py        # Demo site page objects
├── test_practice_sites.py  # Practice automation tests
└── test_demo_practice.py   # Demo site tests
```

## ⚡ New Page Object Template
```python
from playwright.sync_api import Page
from .base_page import BasePage

class NewPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.main_element = "selector"
    
    def main_action(self):
        self.click_element(self.main_element)
```

## ⚡ New Test Template  
```python
from pages.login_page import LoginPage
from pages.new_page import NewPage

def test_new_feature(page: Page):
    # Navigate to practice site
    login_page = PracticeLoginPage(page)
    login_page.navigate_to_login()
    login_page.login_with_valid_credentials()
    
    # Test new feature
    new_page = NewPage(page)
    # Your test code here
```

## 🎯 Practice Site Specific Patterns
```python
# Wait for practice site elements
page.wait_for_selector(".post-title")
page.wait_for_selector("#confirmation")

# Use practice site selectors
"#username"
"#password" 
"#submit"
"#add_btn"

# Handle multiple elements
page.locator("selector").first.click()
```

## 📊 Practice Site Credentials
```python
# Practice Test Automation
URL: "https://practicetestautomation.com/practice-test-login/"
Username: "student"  
Password: "Password123"

# Sauce Demo
URL: "https://www.saucedemo.com/"
Username: "standard_user"
Password: "secret_sauce"
```

## 🔄 Daily Workflow
1. `cd ~/automation-practice/playwright-practice-automation` 
2. `./run_tests.sh` (verify everything working)
3. Work on new features/tests
4. `./run_tests.sh tests/new_test.py -v --headed` (test new code)
5. `./run_tests.sh` (run full suite before committing)

## 🔐 **IMPORTANT: Environment Setup**
```bash
# No .env file needed! All practice sites use public test accounts
# Optional: Create .env only for custom timeout settings
cp .env.example .env  # Only if you want to customize browser settings

# The ./run_tests.sh script works without .env for practice sites
```

---
**💡 Tip**: Keep this card open while developing!
**📚 For detailed explanations, see `PRACTICE_PLAYWRIGHT_DAILY_REFERENCE.md`**