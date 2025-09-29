# D2L Playwright Testing with Page Object Model

A comprehensive test automation framework for D2L (Desire2Learn) using Playwright and Python, built exclusively with the Page Object Model design pattern.

## 🎯 Project Philosophy

This project is **100% Page Object Model (POM)** focused, following industry best practices for maintainable, scalable test automation.

## 📁 Project Structure

```
playwright-ui-python/
├── tests/
│   ├── pages/                          # Page Object Model classes
│   │   ├── __init__.py                # Package initialization
│   │   ├── base_page.py               # Base class for all pages
│   │   ├── login_page.py              # Login & Dashboard pages
│   │   ├── navigation_page.py         # Navigation functionality
│   │   └── course_page.py             # Course-specific actions
│   ├── test_login_pom.py              # Original POM login tests
│   ├── test_d2l_pom_comprehensive.py # Advanced POM tests
│   └── archived_non_pom_tests/        # Archived direct tests
├── examples/                          # Learning examples (non-POM)
├── screenshots/                       # Test screenshots
├── requirements.txt                   # Dependencies
├── pyproject.toml                    # Pytest configuration
└── README_POM.md                     # This file
```

## 🏗️ Page Object Model Architecture

### Base Page Class
All page objects inherit from `BasePage` which provides:
- Common navigation methods
- Element interaction helpers
- Wait strategies
- Assertion utilities
- Screenshot capabilities

### Page Objects Hierarchy

```python
BasePage (base_page.py)
├── LoginPage (login_page.py)
├── DashboardPage (login_page.py)  
├── NavigationPage (navigation_page.py)
└── CoursePage (course_page.py)
```

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies (already done)
pip install -r requirements.txt

# Install Playwright browsers (already done)
playwright install
```

### 2. Run POM Tests
```bash
# Run all POM tests
pytest tests/test_*.py -v --headed

# Run specific test class
pytest tests/test_d2l_pom_comprehensive.py::TestD2LAuthentication -v --headed

# Run single test with debugging
pytest tests/test_login_pom.py::test_successful_login_with_pom -v --headed -s
```

## 🎓 Page Object Model Examples

### Basic Login Test
```python
from pages import LoginPage, DashboardPage

def test_login(page: Page):
    # Initialize page objects
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    # Use page object methods
    login_page.navigate_to_login()
    login_page.login_with_valid_credentials()
    
    # Verify with page object assertions
    assert dashboard_page.is_logged_in()
```

### Advanced Navigation Test
```python
from pages import LoginPage, NavigationPage, CoursePage

def test_navigation_workflow(page: Page):
    # Login first
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login_with_valid_credentials()
    
    # Navigate using page objects
    nav_page = NavigationPage(page)
    nav_page.navigate_to_courses()
    
    # Interact with course page
    course_page = CoursePage(page)
    assert course_page.is_in_course()
```

## 🔧 Available Page Objects

### LoginPage
- `navigate_to_login()` - Go to login page
- `login(username, password)` - Complete login
- `login_with_valid_credentials()` - Login with default creds
- `verify_login_page_elements()` - Verify page elements
- `is_on_login_page()` - Check current page

### DashboardPage  
- `is_logged_in()` - Verify successful login
- `is_on_dashboard()` - Check if on dashboard
- `verify_dashboard_elements()` - Verify page elements
- `logout()` - Logout from D2L

### NavigationPage
- `navigate_to_home()` - Go to home page
- `navigate_to_courses()` - Go to courses
- `navigate_to_calendar()` - Go to calendar  
- `search_for(term)` - Search functionality
- `verify_navigation_elements()` - Verify nav elements

### CoursePage
- `get_course_title()` - Get current course title
- `navigate_to_content()` - Go to course content
- `navigate_to_assignments()` - Go to assignments
- `is_in_course()` - Verify in course context

### BasePage (inherited by all)
- `navigate_to(path)` - Navigate to any path
- `wait_for_page_load()` - Wait for full load
- `click_element(selector)` - Safe click with wait
- `fill_field(selector, value)` - Safe fill with wait
- `take_screenshot(name)` - Capture screenshot
- `assert_url_contains(text)` - URL verification

## 📝 Test Organization

### Test Classes Structure
```python
class TestD2LAuthentication:
    """All authentication-related tests"""
    
class TestD2LNavigation:  
    """All navigation-related tests"""
    
class TestD2LUtilityMethods:
    """Tests for utility methods"""
```

### Fixtures for Reusable Setup
```python
@pytest.fixture(autouse=True)
def login_first(self, page: Page):
    """Auto-login before navigation tests"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login_with_valid_credentials()
```

## 🎯 Best Practices Implemented

### 1. **Single Responsibility** 
Each page object handles only one page/component

### 2. **DRY (Don't Repeat Yourself)**
Common functionality in `BasePage` class

### 3. **Encapsulation**
Selectors and logic hidden inside page objects

### 4. **Readable Tests**
Tests read like business workflows

### 5. **Maintainable Code**
Change selectors in one place, not throughout tests

## 🔍 Running Different Test Scenarios

### Authentication Tests
```bash
pytest tests/test_d2l_pom_comprehensive.py::TestD2LAuthentication -v --headed
```

### Navigation Tests  
```bash
pytest tests/test_d2l_pom_comprehensive.py::TestD2LNavigation -v --headed
```

### Original POM Tests
```bash
pytest tests/test_login_pom.py -v --headed
```

### All POM Tests
```bash
pytest tests/test_*.py -v --headed
```

## 🛠️ Extending the Framework

### Adding New Page Objects
1. Create new page class inheriting from `BasePage`
2. Add selectors and methods for that page
3. Import in `tests/pages/__init__.py`
4. Create tests using the new page object

### Example: Adding a GradesPage
```python
# tests/pages/grades_page.py
from .base_page import BasePage

class GradesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.grades_table = ".d2l-grades-table"
        
    def get_grade_for_assignment(self, assignment_name):
        # Implementation here
        pass
```

## 🎭 Why Page Object Model?

### ✅ Benefits You Get:
- **Maintainable**: Change UI selectors in one place
- **Reusable**: Page objects work across multiple tests  
- **Readable**: Tests describe business workflows
- **Scalable**: Easy to add new pages and functionality
- **Reliable**: Consistent wait strategies and error handling

### ❌ What We Eliminated:
- Code duplication across tests
- Hardcoded selectors in test files  
- Difficult maintenance when UI changes
- Unclear test intentions
- Inconsistent element interactions

## 🚀 Next Steps

1. **Explore the existing tests** to understand the patterns
2. **Add new page objects** for additional D2L pages you need to test
3. **Create test suites** for different workflows
4. **Extend base page functionality** as needed
5. **Add data-driven tests** using the page objects

Your D2L test automation framework is now fully structured with industry-standard Page Object Model patterns! 🎉