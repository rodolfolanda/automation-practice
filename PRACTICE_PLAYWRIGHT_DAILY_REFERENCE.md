# Playwright Practice Automation - Daily Reference Guide

## Table of Contents
1. [Project Setup & Environment](#project-setup--environment)
2. [Daily Development Commands](#daily-development-commands)
3. [Running Tests](#running-tests)
4. [Page Object Model Structure](#page-object-model-structure)
5. [Creating New Page Objects](#creating-new-page-objects)
6. [Writing New Tests](#writing-new-tests)
7. [Debugging & Troubleshooting](#debugging--troubleshooting)
8. [Browser Management](#browser-management)
9. [Common Patterns & Examples](#common-patterns--examp## 🚀 **QUICK START - Daily Workflow** 

### **🎯 RECOMMENDED: Use Easy Commands**
```bash
# 1. Navigate to project
cd ~/automation-practice/playwright-practice-automation

# 2. Run all tests (activates venv automatically)
./run_tests.sh

# 3. Run specific tests  
./run_tests.sh tests/test_practice_sites.py -v --headed

# 4. Debug issues
./run_tests.sh tests/failing_test.py -v -s --headed --slowmo=1000

# 5. Test new features
./run_tests.sh tests/test_new_feature.py -v --headed
```

### **📋 Manual Commands (if run_tests.sh not available)**
```bash
# 1. Activate environment
cd ~/automation-practice/playwright-practice-automation && source venv/bin/activate

# 2. Run tests to verify everything works  
PYTHONPATH=/Users/rlanda/automation-practice/playwright-practice-automation/tests pytest tests/test_practice_sites.py -v --headed

# 3. Run comprehensive tests
PYTHONPATH=/Users/rlanda/automation-practice/playwright-practice-automation/tests pytest tests/test_practice_sites.py -v

# 4. Work on new features
PYTHONPATH=/Users/rlanda/automation-practice/playwright-practice-automation/tests pytest tests/test_new_feature.py -v --headed
```tices](#best-practices)

---

## Project Setup & Environment

### 🔐 **Practice Site Setup (No Credentials Needed!)**
```bash
# This project uses public practice sites - no sensitive credentials!
# All test accounts are built into the code for safety

# Practice sites used:
# - https://practicetestautomation.com/practice/ (student/Password123)
# - https://the-internet.herokuapp.com/ (tomsmith/SuperSecretPassword!)
# - https://www.saucedemo.com/ (standard_user/secret_sauce)
# - https://demo.playwright.dev/ (no login required)

# Optional: Create .env for custom configuration
cp .env.example .env  # Only if you want to customize timeouts, etc.
```

### Initial Setup (One-time)
```bash
# Create project directory
mkdir -p ~/automation-practice/playwright-practice-automation
cd ~/automation-practice/playwright-practice-automation

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Playwright
pip install playwright pytest-playwright

# Install browsers (includes Chrome 140)
playwright install

# Verify installation
playwright --version
```

### Daily Environment Activation
```bash
# Navigate to project
cd ~/automation-practice/playwright-practice-automation

# Activate virtual environment
source venv/bin/activate

# Verify you're in the right environment
which python  # Should show path with /venv/bin/python

# RECOMMENDED: Use the convenience script (handles everything automatically)
./run_tests.sh
```

---

## Daily Development Commands

### Essential Commands You'll Use Every Day

#### 1. **Run All Tests (EASY WAY - RECOMMENDED)**
```bash
# 🚀 Simple test runner (handles PYTHONPATH automatically)
./run_tests.sh

# 🚀 Run specific test file  
./run_tests.sh tests/test_login_pom.py -v --headed

# 🚀 Run specific test
./run_tests.sh tests/test_login_pom.py::test_successful_login_with_pom -v --headed

# 🚀 Run comprehensive tests
./run_tests.sh tests/test_d2l_pom_comprehensive.py -v --headed
```

#### 1b. **Manual Commands (if needed)**
```bash
# Manual way (requires setting PYTHONPATH)
PYTHONPATH=/Users/rlanda/automation-practice/playwright-practice-automation/tests pytest tests/test_practice_sites.py -v --headed

# Run specific test class
PYTHONPATH=/Users/rlanda/automation-practice/playwright-practice-automation/tests pytest tests/test_practice_sites.py::TestPracticeLogin -v --headed
```

#### 2. **Run Tests with Different Browsers**
```bash
# 🚀 Easy way with different browsers
./run_tests.sh tests/test_practice_sites.py --browser chromium --headed
./run_tests.sh tests/test_practice_sites.py --browser firefox --headed  
./run_tests.sh tests/test_practice_sites.py --browser webkit --headed

# Manual way (if needed)
PYTHONPATH=/Users/rlanda/automation-practice/playwright-practice-automation/tests pytest tests/test_practice_sites.py --browser chromium --headed
```

#### 3. **Debug Mode**
```bash
# 🚀 Easy debug mode
./run_tests.sh tests/test_practice_sites.py -v -s --headed --slowmo=1000

# 🚀 Debug specific test
./run_tests.sh tests/test_practice_sites.py::TestPracticeLogin::test_successful_login -v -s --headed

# Manual debug (if needed)
PYTHONPATH=/Users/rlanda/automation-practice/playwright-practice-automation/tests pytest tests/test_practice_sites.py -v -s --headed --slowmo=1000
```

#### 4. **Update Dependencies**
```bash
# Update Playwright
pip install --upgrade playwright

# Update browsers (when Playwright updates)
playwright install

# Check for new browser versions
playwright install --help
```

---

## Running Tests

### Test Organization in Your Project

```bash
# Your current test structure:
tests/
├── test_practice_sites.py              # Practice site automation tests
├── test_demo_practice.py                # Playwright demo site tests
└── pages/
    ├── base_page.py                     # Foundation class
    ├── practice_pages.py                # Practice site page objects
    └── demo_page.py                     # Demo site page objects
```

### Common Test Commands

```bash
# Run login practice tests only
pytest tests/test_practice_sites.py::TestPracticeLogin -v --headed

# Run exception handling tests  
pytest tests/test_practice_sites.py::TestPracticeExceptions -v --headed

# Run demo site tests
pytest tests/test_demo_practice.py::TestPlaywrightDemo -v --headed

# Run failed tests only (after a test run)
pytest --lf

# Run last failed test with debug info
pytest --lf -v -s --headed
```

---

## Page Object Model Structure

### Your Current Page Object Hierarchy

```python
# Base class (inherit from this)
class BasePage:
    """Foundation with 20+ utility methods"""
    
    # Navigation methods
    def navigate_to(self, url)
    def go_back(self)
    def refresh_page(self)
    
    # Element interaction
    def click_element(self, selector)
    def fill_field(self, selector, text)
    def get_text(self, selector)
    def is_element_visible(self, selector)
    
    # Assertions
    def assert_url_contains(self, expected_url)
    def assert_page_title(self, expected_title)
    def assert_element_text(self, selector, expected_text)
```

### Current Page Objects

```python
# Practice site functionality
from pages.practice_pages import PracticeLoginPage, PracticeExceptionsPage

# Demo site functionality
from pages.demo_page import PlaywrightDemoPage

# Base functionality (inherited by all)
from pages.base_page import BasePage
```

---

## Creating New Page Objects

### Template for New Page Object

```python
# File: tests/pages/new_page.py
"""
New Page Object for [Practice Site Name] [Feature Name]
Handles [specific functionality] elements and actions
"""

from playwright.sync_api import Page
from .base_page import BasePage

class NewPageName(BasePage):
    """Page Object for [Practice Site] [Feature] functionality"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Define selectors specific to this page
        self.main_element = "selector-for-main-element"
        self.action_button = "button:has-text('Action')"
        self.form_field = "input[name='fieldname']"
        
    def perform_main_action(self):
        """Main action this page performs"""
        self.click_element(self.action_button)
        
    def fill_form(self, data: str):
        """Fill form with data"""
        self.fill_field(self.form_field, data)
        
    def is_on_page(self):
        """Verify we're on the correct page"""
        return self.is_element_visible(self.main_element)
```

### Adding Page Object to Tests

```python
# In your test file
from pages.new_page import NewPageName
from pages.practice_pages import PracticeLoginPage

def test_new_functionality(page: Page):
    """Test new functionality"""
    
    # Login first if needed (for sites that require it)
    login_page = PracticeLoginPage(page)
    login_page.navigate_to_login()
    login_page.login_with_valid_credentials()
    
    # Use new page object
    new_page = NewPageName(page)
    new_page.navigate_to("https://your-practice-site.com/new-section")
    
    assert new_page.is_on_page()
    new_page.perform_main_action()
```

---

## Writing New Tests

### Test File Template

```python
# File: tests/test_new_feature.py
"""
Test suite for [Practice Site] [New Feature] functionality using Page Object Model
"""

import pytest
from playwright.sync_api import Page
from pages.practice_pages import PracticeLoginPage, PracticeExceptionsPage
from pages.new_page import NewPageName

class TestNewFeature:
    """Test class for [New Feature] functionality"""
    
    def test_basic_functionality(self, page: Page):
        """Test basic feature functionality"""
        
        # Navigate to practice site
        new_page = NewPageName(page)
        new_page.navigate_to("https://your-practice-site.com/feature")
        
        # Test new feature
        # Add your test steps here
        
    def test_error_scenarios(self, page: Page):
        """Test error handling"""
        # Similar login pattern + error testing
        pass
        
def test_standalone_feature(page: Page):
    """Standalone test outside class"""
    # Test code here
    pass
```

### Running Your New Tests

```bash
# Run new test file
pytest tests/test_new_feature.py -v --headed

# Run specific test class
pytest tests/test_new_feature.py::TestNewFeature -v --headed

# Run specific test method
pytest tests/test_new_feature.py::TestNewFeature::test_basic_functionality -v --headed
```

---

## Debugging & Troubleshooting

### Common Issues & Solutions

#### 1. **Element Not Found**
```python
# Debug: Check what elements exist
elements = page.locator("your-selector").all()
print(f"Found {len(elements)} elements")

# Use more specific selectors
# Bad: "button"
# Good: "button:has-text('Log In')"
# Better: "button.d2l-button:has-text('Log In')"
```

#### 2. **Timing Issues (Most Common)**
```python
# Always use proper waits for dynamic content
page.wait_for_url("**/practice-test-login/**", timeout=10000)

# Wait for specific elements
page.wait_for_selector("#confirmation")

# Wait for page load
page.wait_for_load_state("networkidle")
```

#### 3. **Multiple Elements Found**
```python
# Use .first for multiple matches
element = page.locator("input[type='submit']").first
element.click()

# Or be more specific with selectors
specific_element = page.locator("#submit")
```

### Debug Commands

```bash
# Run with browser visible and slow motion
pytest --headed --slowmo=1000

# Debug specific failing test
pytest tests/test_practice_sites.py::TestPracticeLogin::test_successful_login -v -s --headed

# See full error traces
pytest --tb=long

# Stop at first failure
pytest -x
```

### Create Debug Scripts

```python
# File: debug_element_finder.py
import asyncio
from playwright.async_api import async_playwright

async def debug_elements():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Navigate to practice site
        await page.goto("https://practicetestautomation.com/practice-test-login/")
        await page.fill("#username", "student")
        await page.fill("#password", "Password123")
        await page.click("#submit")
        
        # Debug elements
        elements = await page.locator(".post-title").all()
        print(f"Found {len(elements)} success elements")
        
        # Keep browser open for inspection
        input("Press Enter to close browser...")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(debug_elements())
```

---

## Browser Management

### Browser-Related Commands

```bash
# Check installed browsers
playwright install --dry-run

# Install specific browser
playwright install chromium
playwright install firefox
playwright install webkit

# Update all browsers
playwright install

# Check Playwright version
playwright --version

# Get browser versions
python -c "
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    print(f'Chromium: {p.chromium.version}')
    print(f'Firefox: {p.firefox.version}') 
    print(f'Webkit: {p.webkit.version}')
"
```

### Browser Configuration in Tests

```python
# pytest.ini or pyproject.toml configuration
[tool.pytest.ini_options]
addopts = "--browser chromium --headed"

# Override in command line
pytest --browser firefox --headed
```

---

## Common Patterns & Examples

### 1. **Standard Test Pattern**
```python
def test_example(page: Page):
    # 1. Navigate to practice site
    page_object = SomePracticePageObject(page)
    page_object.navigate_to_practice_site()
    
    # 2. Perform login if needed
    if page_object.requires_login():
        page_object.login_with_valid_credentials()
    
    # 3. Perform actions
    page_object.perform_action()
    
    # 4. Assert results
    assert page_object.verify_result()
```

### 2. **Practice Site Pattern**
```python
# Navigate to different practice scenarios
login_page = PracticeLoginPage(page)
login_page.navigate_to_login()              # Login practice
login_page.login_with_valid_credentials()   # Valid login

exceptions_page = PracticeExceptionsPage(page)
exceptions_page.navigate_to_exceptions()    # Dynamic elements
exceptions_page.click_add_button()          # Exception handling
```

### 3. **Form Filling Pattern**
```python
# Fill forms using page objects
page_object.fill_field("input[name='title']", "Assignment Title")
page_object.fill_field("textarea[name='description']", "Assignment Description")
page_object.click_element("button:has-text('Save')")
```

### 4. **Error Testing Pattern**
```python
def test_error_scenario(page: Page):
    login_page = PracticeLoginPage(page)
    login_page.navigate_to_login()
    
    # Test invalid credentials
    login_page.login_with_credentials("incorrectUser", "Password123")
    
    # Verify error message
    error_message = login_page.get_error_message()
    assert "Your username is invalid!" in error_message
```

---

## Best Practices

### 1. **Selectors**
```python
# ✅ Good selectors (specific and stable)
"#submit"
"#username"
"#password"
"button:has-text('Add')"

# ❌ Avoid (too generic)
"button"
"div"
"input"
```

### 2. **Wait Strategies**
```python
# ✅ Always use proper waits
page.wait_for_selector("#confirmation")
page.wait_for_selector(".post-title")
page.wait_for_load_state("networkidle")

# ❌ Never use sleep
import time
time.sleep(5)  # Don't do this
```

### 3. **Test Organization**
```python
# ✅ Group related tests in classes
class TestAuthentication:
    def test_valid_login(self):
    def test_invalid_login(self):
    def test_logout(self):

class TestNavigation:
    def test_menu_navigation(self):
    def test_breadcrumbs(self):
```

### 4. **Page Object Methods**
```python
# ✅ Methods should be action-oriented
def login_with_credentials(self, username, password):
def click_add_button(self):
def enter_text_in_second_row(self, text):

# ✅ Include verification methods
def is_logged_in(self):
def is_second_row_visible(self):
def get_confirmation_message(self):
```

---

## Daily Workflow Summary

### Every Day Commands
```bash
# 1. Activate environment
cd ~/automation-practice/playwright-practice-automation && source venv/bin/activate

# 2. Run tests to verify everything works
pytest tests/test_practice_sites.py -v --headed

# 3. Run comprehensive tests
pytest tests/test_practice_sites.py tests/test_demo_practice.py -v

# 4. Work on new features
pytest tests/test_new_feature.py -v --headed

# 5. Debug issues
pytest tests/failing_test.py -v -s --headed --slowmo=1000
```

### Weekly Maintenance
```bash
# Update Playwright and browsers
pip install --upgrade playwright
playwright install

# Run full test suite
pytest -v

# Check for any deprecated methods
pytest --tb=short
```

---

## Extending Your Project

### Adding New Practice Sites

1. **Identify the practice site** (Sauce Demo, The Internet, etc.)
2. **Create page object** (`tests/pages/saucedemo_page.py`)
3. **Write tests** (`tests/test_saucedemo.py`)
4. **Run and debug** (`pytest tests/test_saucedemo.py -v --headed`)

### Example: Adding Sauce Demo Module

```bash
# Create new page object
touch tests/pages/saucedemo_page.py

# Create new test file  
touch tests/test_saucedemo.py

# Run new tests
pytest tests/test_saucedemo.py -v --headed
```

---

**🎯 This reference guide contains everything you need for daily Playwright practice automation development!**

**Bookmark this document and use it as your daily companion for learning and extending your automation skills.**