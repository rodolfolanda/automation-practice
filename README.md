# Playwright Practice Automation# Playwright Practice Automation



Learn Playwright automation using real practice websites! This repository contains comprehensive examples and exercises for mastering web automation with Python and the Page Object Model (POM) architecture.Learn Playwright automation using real practice websites! This repository contains comprehensive examples and exercises for mastering web automation with Python and the Page Object Model (POM) architecture.



## 🎯 Overview## 🎯 Overview



This project provides hands-on learning for Playwright automation using safe practice websites, featuring:This project provides hands-on learning for Playwright automation using safe practice websites, featuring:

- **Page Object Model** architecture for maintainable test code- **Page Object Model** architecture for maintainable test code

- **Multiple practice websites** for different automation scenarios- **Multiple practice websites** for different automation scenarios

- **Cross-browser compatibility** (Chrome, Firefox, Safari)- **Cross-browser compatibility** (Chrome, Firefox, Safari)

- **Real-world patterns** without sensitive data or credentials- **Real-world patterns** without sensitive data or credentials

- **Progressive learning** from basic to advanced automation techniques- **Progressive learning** from basic to advanced automation techniques



## 🚀 Quick Start## 🚀 Quick Start



### 1. Clone and Setup### 1. Clone and Setup

```bash```bash

git clone https://github.com/rodolfolanda/automation-practice.gitgit clone https://github.com/rodolfolanda/automation-practice.git

cd automation-practicecd automation-practice

python3 -m venv .venvpython3 -m venv .venv

source .venv/bin/activatesource .venv/bin/activate

pip install -r requirements.txtpip install -r requirements.txt

playwright installplaywright install

``````



### 2. Run Practice Tests### 2. Run Practice Tests

```bash```bash

./run_tests.sh                           # Run all tests./run_tests.sh                           # Run all tests

./run_tests.sh tests/test_practice_sites.py   # Run practice tests./run_tests.sh tests/test_practice_sites.py   # Run practice tests

``````



### 3. Run in Headed Mode (Visual)### 3. Run in Headed Mode (Visual)

```bash```bash

pytest tests/ --headed -v               # See browsers in actionpytest tests/ --headed -v               # See browsers in action

``````



## 📁 Project Structure## � Project Structure



``````

automation-practice/automation-practice/

├── ⚙️  config.py                        # Configuration for practice sites├── ⚙️  config.py                        # Configuration for practice sites

├── 🚀 run_tests.sh                      # Convenience test runner├── 🚀 run_tests.sh                      # Convenience test runner

├── 🔍 playwright_linter.py              # Code quality checker├── 🔍 playwright_linter.py              # Code quality checker

├── 📚 PRACTICE_PLAYWRIGHT_DAILY_REFERENCE.md # Complete reference guide├── 📚 PRACTICE_PLAYWRIGHT_DAILY_REFERENCE.md # Complete reference guide

├── ⚡ QUICK_REFERENCE_CARD.md           # Essential commands├── ⚡ QUICK_REFERENCE_CARD.md           # Essential commands

├── tests/                              # Test automation code├── tests/                              # Test automation code

│   ├── pages/                          # Page Object Model│   ├── pages/                          # Page Object Model

│   │   ├── base_page.py               # Foundation class│   │   ├── base_page.py               # Foundation class

│   │   └── practice_pages.py          # Practice site pages│   │   ├── login_page.py              # Login & Dashboard

│   └── test_practice_sites.py         # Practice automation tests│   │   ├── navigation_page.py         # D2L navigation

├── requirements.txt                    # Dependencies│   │   └── course_page.py             # Course functionality

└── pyproject.toml                     # Project configuration│   ├── test_login_pom.py              # Basic POM tests

```│   └── test_d2l_pom_comprehensive.py  # Full test suite

├── requirements.txt                    # Dependencies

## 🏗️ Page Object Model Architecture└── pyproject.toml                     # Project configuration

```

This project uses the **Page Object Model** design pattern for maintainable and scalable test automation:

## �️ Page Object Model Architecture

### **BasePage** - Foundation Class

```pythonThis project uses the **Page Object Model** design pattern for maintainable and scalable test automation:

class BasePage:

    def navigate_to(self, url)### **BasePage** - Foundation Class

    def click_element(self, selector)```python

    def fill_field(self, selector, text)class BasePage:

    def assert_url_contains(self, expected_url)    def navigate_to(self, url)

    # ... 20+ utility methods    def click_element(self, selector)

```    def fill_field(self, selector, text)

    def assert_url_contains(self, expected_url)

### **PracticeLoginPage** - Practice Authentication    # ... 20+ utility methods

```python```

class PracticeLoginPage(BasePage):

    def navigate_to_login(self)### **LoginPage** - D2L Authentication

    def login_with_valid_credentials(self)```python

    def login_with_credentials(self, username, password)class LoginPage(BasePage):

    def get_error_message(self)    def navigate_to_login(self)

```    def login_with_valid_credentials(self)  # Uses env variables

    def enter_username(self, username)

## 🧪 Test Coverage    def enter_password(self, password)

```

### **Practice Login Tests** (4 tests) ✅

- ✅ Successful login flow### **NavigationPage** - D2L Navigation

- ✅ Invalid username handling```python

- ✅ Invalid password handlingclass NavigationPage(BasePage):

- ✅ Step-by-step login process    def navigate_to_quick_eval(self)

    def navigate_to_calendar(self)

### **Practice Exception Tests** (3 tests)    def verify_navigation_elements(self)

- 🔄 Add dynamic elements```

- 🔄 Delete elements

- 🔄 Exception handling## 🧪 Test Coverage



### **Total: 7 Tests** - Safe practice automation with no credentials needed### **Authentication Tests** (3 tests)

- ✅ Successful login with POM

## 🌐 Practice Sites Used- ✅ Invalid login handling  

- ✅ Step-by-step login process

- **[Practice Test Automation](https://practicetestautomation.com/)** - Login and exceptions practice

- **[The Internet](https://the-internet.herokuapp.com/)** - Various automation challenges### **Comprehensive Test Suite** (8 tests)

- **[Sauce Demo](https://www.saucedemo.com/)** - E-commerce testing scenarios- ✅ D2L Authentication workflows

- ✅ Navigation element verification

All sites are designed for automation practice and don't require real credentials!- ✅ User workflow journeys

- ✅ Utility method validation

## 🔧 Daily Commands- ✅ Error handling scenarios



### **Easy Way (Recommended)**### **Total: 11 Tests** - All passing with Chrome 140 compatibility

```bash

./run_tests.sh                              # Run all tests## 🔐 Security Features

./run_tests.sh tests/test_practice_sites.py # Run practice tests

./run_tests.sh --browser firefox --headed  # Different browser### **Environment Variables**

``````bash

# .env file (gitignored)

### **Manual Commands**D2L_BASE_URL=https://your-d2l-instance.com/

```bashD2L_USERNAME=your-username

# Run specific test classD2L_PASSWORD=your-password

pytest tests/test_practice_sites.py::TestPracticeLogin -v```



# Cross-browser testing### **No Hardcoded Credentials**

pytest --browser chromium --browser firefox --browser webkit```python

# Secure credential loading from environment

# Debug mode with visual feedbackfrom config import config

pytest -v -s --headed --slowmo=1000username, password = config.get_d2l_credentials()

``````



## 🛠️ Development Tools## 🔧 Daily Commands



### **Code Quality**### **Easy Way (Recommended)**

```bash```bash

python playwright_linter.py tests/  # Check Playwright best practices./run_tests.sh                              # Run all tests

```./run_tests.sh tests/test_login_pom.py      # Run specific file  

./run_tests.sh --browser firefox --headed  # Different browser

### **Browser Management**```

```bash

playwright install          # Install/update all browsers### **Manual Commands**

playwright install chromium # Install specific browser```bash

playwright --version        # Check version# Set Python path and run tests

```PYTHONPATH=/path/to/tests pytest tests/test_login_pom.py -v --headed



## 📚 Key Practice Patterns# Cross-browser testing

pytest --browser chromium --browser firefox --browser webkit

### **Safe Practice Login**

```python# Debug mode

def test_practice_login(page):pytest -v -s --headed --slowmo=1000

    login_page = PracticeLoginPage(page)```

    login_page.navigate_to_login()

    login_page.login_with_valid_credentials()  # Uses known practice credentials## 🛠️ Development Tools

    

    # Verify success page### **Code Quality**

    assert "Logged In Successfully" in page.text_content("body")```bash

```python playwright_linter.py tests/  # Check Playwright best practices

```

### **Exception Handling Practice**

```python### **Browser Management**

def test_element_interactions(page):```bash

    exceptions_page = PracticeExceptionsPage(page)playwright install          # Install/update all browsers

    exceptions_page.navigate_to_exceptions()playwright install chromium # Install specific browser

    exceptions_page.click_add_button()playwright --version        # Check version

    assert exceptions_page.is_second_row_visible()```

```

## 📚 Key D2L Patterns

## 🔒 Security Features

### **Secure Login Pattern**

- **No Real Credentials**: All practice sites use known test credentials```python

- **Safe Practice Sites**: No risk of affecting real applicationsdef test_d2l_login(page):

- **Git Security**: No sensitive data in repository    login_page = LoginPage(page)

- **Learning Focused**: Perfect for skill development    login_page.navigate_to_login()

    login_page.login_with_valid_credentials()  # Uses env variables

## 🌐 Browser Support    

    # Wait for D2L redirects

Tested and verified on:    page.wait_for_url("**/d2l/home**", timeout=10000)

- **Chromium** (Latest Chrome compatibility)```

- **Firefox** (Cross-browser validation)

- **WebKit/Safari** (Mobile Safari simulation)### **D2L Navigation Pattern**

```python

## 📈 Quality Assurancedef test_d2l_navigation(page):

    navigation_page = NavigationPage(page)

- **Custom Linting**: `playwright_linter.py` enforces Playwright best practices    navigation_page.navigate_to_quick_eval()

- **Page Object Model**: 100% POM architecture for maintainability    navigation_page.navigate_to_calendar()

- **Test Isolation**: Each test runs independently with clean state```

- **Practice Safe**: No real applications affected

### **D2L Selectors**

## 🚀 Next Stepspage.locator("#my-id")

page.locator(".my-class")

1. **Run the test suite** with `./run_tests.sh`page.locator("button")

2. **Explore practice sites** to understand the test scenarios

3. **Extend page objects** for additional practice functionality# Text content

4. **Add new test scenarios** following the established POM pattern# D2L-specific element patterns

5. **Practice different browsers** with cross-browser testing"[data-automation-id='']"     # D2L automation IDs

".d2l-navigation-s-"          # D2L navigation classes  

## 🎓 Learning Path"d2l-dropdown-menu"           # D2L dropdown components

```

1. **Start with Login Tests**: Understand basic form interactions

2. **Try Exception Handling**: Learn dynamic element management## 🧪 Test Coverage

3. **Explore Different Sites**: Practice various automation scenarios

4. **Write Custom Tests**: Create your own test cases### **Login & Authentication Tests** (`test_login_pom.py`)

5. **Advanced Patterns**: API testing, visual testing, performance- Valid credential login

- Dashboard navigation after login

---- Authentication flow validation



**Perfect for Learning** 🎓 | **Safe Practice** 🛡️ | **Real Automation** 🎭### **Comprehensive D2L Tests** (`test_d2l_pom_comprehensive.py`) 
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