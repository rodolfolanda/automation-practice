# Playwright Practice Automation

Learn Playwright automation using real practice websites! This repository contains comprehensive examples and exercises for mastering web automation with Python and the Page Object Model (POM) architecture.

## 🎯 Overview

This project provides hands-on learning for Playwright automation using safe practice websites, featuring:
- **Page Object Model** architecture for maintainable test code
- **Multiple practice websites** for different automation scenarios
- **Cross-browser compatibility** (Chrome, Firefox, Safari)
- **Real-world patterns** without sensitive data or credentials
- **Progressive learning** from basic to advanced automation techniques

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone <your-repo-url>
cd d2l-automation-project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
```

### 2. Configure Credentials
```bash
cp .env.example .env
# Edit .env with your D2L credentials:
# D2L_USERNAME=your-username
# D2L_PASSWORD=your-password
```

### 3. Run Tests (Easy Way)
```bash
./run_tests.sh                           # Run all tests
./run_tests.sh tests/test_login_pom.py   # Run specific test file
```

## 📁 Project Structure

```
d2l-playwright-automation/
├── 🔐 .env                              # Your credentials (gitignored)
├── 📋 .env.example                      # Credential template
├── ⚙️  config.py                        # Configuration management
├── 🚀 run_tests.sh                      # Convenience test runner
├── 🔍 playwright_linter.py              # Code quality checker
├── 📚 D2L_PLAYWRIGHT_DAILY_REFERENCE.md # Complete reference guide
├── ⚡ QUICK_REFERENCE_CARD.md           # Essential commands
├── tests/                              # Test automation code
│   ├── pages/                          # Page Object Model
│   │   ├── base_page.py               # Foundation class
│   │   ├── login_page.py              # Login & Dashboard
│   │   ├── navigation_page.py         # D2L navigation
│   │   └── course_page.py             # Course functionality
│   ├── test_login_pom.py              # Basic POM tests
│   └── test_d2l_pom_comprehensive.py  # Full test suite
├── requirements.txt                    # Dependencies
└── pyproject.toml                     # Project configuration
```

## �️ Page Object Model Architecture

This project uses the **Page Object Model** design pattern for maintainable and scalable test automation:

### **BasePage** - Foundation Class
```python
class BasePage:
    def navigate_to(self, url)
    def click_element(self, selector)
    def fill_field(self, selector, text)
    def assert_url_contains(self, expected_url)
    # ... 20+ utility methods
```

### **LoginPage** - D2L Authentication
```python
class LoginPage(BasePage):
    def navigate_to_login(self)
    def login_with_valid_credentials(self)  # Uses env variables
    def enter_username(self, username)
    def enter_password(self, password)
```

### **NavigationPage** - D2L Navigation
```python
class NavigationPage(BasePage):
    def navigate_to_quick_eval(self)
    def navigate_to_calendar(self)
    def verify_navigation_elements(self)
```

## 🧪 Test Coverage

### **Authentication Tests** (3 tests)
- ✅ Successful login with POM
- ✅ Invalid login handling  
- ✅ Step-by-step login process

### **Comprehensive Test Suite** (8 tests)
- ✅ D2L Authentication workflows
- ✅ Navigation element verification
- ✅ User workflow journeys
- ✅ Utility method validation
- ✅ Error handling scenarios

### **Total: 11 Tests** - All passing with Chrome 140 compatibility

## 🔐 Security Features

### **Environment Variables**
```bash
# .env file (gitignored)
D2L_BASE_URL=https://your-d2l-instance.com/
D2L_USERNAME=your-username
D2L_PASSWORD=your-password
```

### **No Hardcoded Credentials**
```python
# Secure credential loading from environment
from config import config
username, password = config.get_d2l_credentials()
```

## 🔧 Daily Commands

### **Easy Way (Recommended)**
```bash
./run_tests.sh                              # Run all tests
./run_tests.sh tests/test_login_pom.py      # Run specific file  
./run_tests.sh --browser firefox --headed  # Different browser
```

### **Manual Commands**
```bash
# Set Python path and run tests
PYTHONPATH=/path/to/tests pytest tests/test_login_pom.py -v --headed

# Cross-browser testing
pytest --browser chromium --browser firefox --browser webkit

# Debug mode
pytest -v -s --headed --slowmo=1000
```

## 🛠️ Development Tools

### **Code Quality**
```bash
python playwright_linter.py tests/  # Check Playwright best practices
```

### **Browser Management**
```bash
playwright install          # Install/update all browsers
playwright install chromium # Install specific browser
playwright --version        # Check version
```

## 📚 Key D2L Patterns

### **Secure Login Pattern**
```python
def test_d2l_login(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login_with_valid_credentials()  # Uses env variables
    
    # Wait for D2L redirects
    page.wait_for_url("**/d2l/home**", timeout=10000)
```

### **D2L Navigation Pattern**
```python
def test_d2l_navigation(page):
    navigation_page = NavigationPage(page)
    navigation_page.navigate_to_quick_eval()
    navigation_page.navigate_to_calendar()
```

### **D2L Selectors**
page.locator("#my-id")
page.locator(".my-class")
page.locator("button")

# Text content
# D2L-specific element patterns
"[data-automation-id='']"     # D2L automation IDs
".d2l-navigation-s-"          # D2L navigation classes  
"d2l-dropdown-menu"           # D2L dropdown components
```

## 🧪 Test Coverage

### **Login & Authentication Tests** (`test_login_pom.py`)
- Valid credential login
- Dashboard navigation after login
- Authentication flow validation

### **Comprehensive D2L Tests** (`test_d2l_pom_comprehensive.py`) 
- Full navigation workflow
- Quick Eval access
- Calendar functionality
- Course navigation
- User profile access
- Menu interactions
- Mobile responsive testing
- Multi-step user journeys

## 🔒 Security Features

- **Environment Variables**: All credentials stored securely
- **No Hardcoded Secrets**: Clean codebase for team sharing
- **Config Validation**: Automatic credential validation on startup
- **Git Security**: .env files excluded from repository

## 🌐 Browser Support

Tested and verified on:
- **Chromium 140.0.7339.16** (Latest Chrome compatibility)
- **Firefox** (Cross-browser validation)
- **WebKit/Safari** (Mobile Safari simulation)

## 📈 Quality Assurance

- **Custom Linting**: `playwright_linter.py` enforces Playwright best practices
- **Page Object Model**: 100% POM architecture for maintainability  
- **Environment Validation**: Automatic config validation prevents runtime issues
- **Test Isolation**: Each test runs independently with clean state

## 🚀 Next Steps

1. **Set up environment variables** in `.env` file
2. **Run the test suite** with `./run_tests.sh`
3. **Extend page objects** for additional D2L functionality
4. **Add new test scenarios** following the established POM pattern
5. **Integrate with CI/CD** for automated testing

---

**Ready for Production** ✅ | **Team Collaboration** 🤝 | **D2L Integration** 📚
page.get_by_text("Click me")

# Attributes
page.locator("[data-testid='submit-button']")
page.get_by_test_id("submit-button")

# Role-based selectors
page.get_by_role("button", name="Submit")
page.get_by_label("Email address")
```

### Waiting Strategies
```python
# Wait for element to be visible
page.wait_for_selector("#element")

# Wait for network to be idle
page.wait_for_load_state("networkidle")

# Wait for specific condition
page.wait_for_function("window.jQuery !== undefined")
```

### Browser Contexts
```python
# Create isolated browser context
context = browser.new_context(
    viewport={"width": 1920, "height": 1080},
    user_agent="Custom User Agent",
    locale="en-US",
    timezone_id="America/New_York"
)
```

## 🛠️ Advanced Features

### Screenshots and Videos
```python
# Full page screenshot
page.screenshot(path="screenshot.png", full_page=True)

# Element screenshot
element.screenshot(path="element.png")

# Record video (automatically in test mode)
# Videos saved to test-results/
```

### Mobile Emulation
```python
# iPhone 12 Pro
context = browser.new_context(**playwright.devices["iPhone 12 Pro"])

# Custom mobile viewport
context = browser.new_context(
    viewport={"width": 375, "height": 812},
    user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)...",
    is_mobile=True,
    has_touch=True
)
```

### Network Interception
```python
# Block images
page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())

# Mock API responses
def handle_api(route):
    route.fulfill(json={"status": "success"})

page.route("**/api/**", handle_api)
```

## 🔍 Debugging Tips

1. **Use `page.pause()`** to pause execution and interact with the browser manually
2. **Set `headless=False`** to see what's happening in the browser
3. **Use `slow_mo`** parameter to slow down actions
4. **Take screenshots** at different steps to see page state
5. **Check browser console** with `page.on("console", lambda msg: print(msg.text))`

## 📖 Next Steps

1. **Read the Official Docs**: [https://playwright.dev/python/](https://playwright.dev/python/)
2. **Try the Examples**: Run each example script and modify them
3. **Write Your Own Tests**: Create tests for websites you use regularly
4. **Explore Advanced Features**: API testing, visual comparisons, performance metrics
5. **Learn Page Object Model**: Organize your test code better

## 🤝 Common Use Cases

- **E2E Testing**: Test complete user workflows
- **Regression Testing**: Ensure changes don't break existing functionality
- **Cross-Browser Testing**: Verify compatibility across browsers
- **Performance Testing**: Measure page load times and interactions
- **Visual Testing**: Compare screenshots to detect visual regressions
- **Web Scraping**: Extract data from websites
- **Automation**: Automate repetitive web tasks

## 🆘 Troubleshooting

### Browser Installation Issues
```bash
# Reinstall browsers
playwright install

# Install specific browser
playwright install chromium
```

### Common Errors
- **Element not found**: Use proper waiting strategies
- **Timeout errors**: Increase timeout values or improve selectors
- **Flaky tests**: Add explicit waits instead of sleep()

Happy testing with Playwright! 🎭