# Playwright Practice Automation

Learn Playwright automation using real practice websites! This repository contains comprehensive examples and exercises for mastering web automation with Python and the Page Object Model (POM) architecture.

## 🎯 Overview

This project provides hands-on learning for Playwright automation using safe practice websites, featuring:
- **Page Object Model** architecture for maintainable test code
- **Multiple practice websites** for different automation scenarios
- **Cross-browser compatibility** (Chrome, Firefox, Safari)
- **Real-world patterns** without sensitive data or credentials
- **Progressive learning** from basic to advanced automation techniques

## 🤖 Development Approach

This project showcases **AI-Assisted Learning and Development**:

- **100% AI-Generated Code**: All Python and Playwright automation code written by GitHub Copilot (Claude Sonnet 4)
- **Prompt Engineering Learning**: Demonstrates effective prompt engineering techniques for learning Python and Playwright automation
- **Educational Philosophy**: Learning through intelligent collaboration between human guidance and AI code generation

This approach allows rapid skill acquisition by focusing on **understanding automation concepts** and **effective communication with AI tools**, rather than syntax memorization.

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone https://github.com/rodolfolanda/automation-practice.git
cd automation-practice
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

### 2. Run Practice Tests
```bash
./run_tests.sh                           # Run all tests
./run_tests.sh tests/test_practice_sites.py   # Run practice tests
```

### 3. Run in Headed Mode (Visual)
```bash
pytest tests/ --headed -v               # See browsers in action
```

## 📁 Project Structure

```
automation-practice/
├── ⚙️  config.py                        # Configuration for practice sites
├── 🚀 run_tests.sh                      # Convenience test runner
├── 🔍 playwright_linter.py              # Code quality checker
├── 📚 PRACTICE_PLAYWRIGHT_DAILY_REFERENCE.md # Complete reference guide
├── ⚡ QUICK_REFERENCE_CARD.md           # Essential commands
├── tests/                              # Test automation code
│   ├── pages/                          # Page Object Model
│   │   ├── base_page.py               # Foundation class
│   │   └── practice_pages.py          # Practice site pages
│   └── test_practice_sites.py         # Practice automation tests
├── requirements.txt                    # Dependencies
└── pyproject.toml                     # Project configuration
```

## 🏗️ Page Object Model Architecture

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

### **PracticeLoginPage** - Practice Authentication
```python
class PracticeLoginPage(BasePage):
    def navigate_to_login(self)
    def login_with_valid_credentials(self)
    def login_with_credentials(self, username, password)
    def get_error_message(self)
```

## 🧪 Test Coverage

### **Practice Login Tests** (4 tests) ✅
- ✅ Successful login flow
- ✅ Invalid username handling
- ✅ Invalid password handling
- ✅ Step-by-step login process

### **Practice Exception Tests** (3 tests) ✅
- ✅ Add dynamic elements
- ✅ Remove elements with confirmation
- ✅ Exception handling scenarios

### **Total: 7 Tests** - Safe practice automation with no credentials needed

## 🌐 Practice Sites Used

- **[Practice Test Automation](https://practicetestautomation.com/)** - Login and exceptions practice
- **[The Internet](https://the-internet.herokuapp.com/)** - Various automation challenges
- **[Sauce Demo](https://www.saucedemo.com/)** - E-commerce testing scenarios

All sites are designed for automation practice and don't require real credentials!

## 🔧 Daily Commands

### **Easy Way (Recommended)**
```bash
./run_tests.sh                              # Run all tests
./run_tests.sh tests/test_practice_sites.py # Run practice tests
./run_tests.sh --browser firefox --headed  # Different browser
```

### **Manual Commands**
```bash
# Run specific test class
pytest tests/test_practice_sites.py::TestPracticeLogin -v

# Cross-browser testing
pytest --browser chromium --browser firefox --browser webkit

# Debug mode with visual feedback
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

## 📚 Key Practice Patterns

### **Safe Practice Login**
```python
def test_practice_login(page):
    login_page = PracticeLoginPage(page)
    login_page.navigate_to_login()
    login_page.login_with_valid_credentials()  # Uses known practice credentials
    
    # Verify success page
    assert "Logged In Successfully" in page.text_content("body")
```

### **Exception Handling Practice**
```python
def test_element_interactions(page):
    exceptions_page = PracticeExceptionsPage(page)
    exceptions_page.navigate_to_exceptions()
    exceptions_page.click_add_button()
    assert exceptions_page.is_second_row_visible()
```

## 🔒 Security Features

- **No Real Credentials**: All practice sites use known test credentials
- **Safe Practice Sites**: No risk of affecting real applications
- **Git Security**: No sensitive data in repository
- **Learning Focused**: Perfect for skill development

## 🌐 Browser Support

Tested and verified on:
- **Chromium** (Latest Chrome compatibility)
- **Firefox** (Cross-browser validation)
- **WebKit/Safari** (Mobile Safari simulation)

## 📈 Quality Assurance

- **Custom Linting**: `playwright_linter.py` enforces Playwright best practices
- **Page Object Model**: 100% POM architecture for maintainability
- **Test Isolation**: Each test runs independently with clean state
- **Practice Safe**: No real applications affected

## 🚀 Next Steps

1. **Run the test suite** with `./run_tests.sh`
2. **Explore practice sites** to understand the test scenarios
3. **Extend page objects** for additional practice functionality
4. **Add new test scenarios** following the established POM pattern
5. **Practice different browsers** with cross-browser testing

## 🎓 Learning Path

1. **Start with Login Tests**: Understand basic form interactions
2. **Try Exception Handling**: Learn dynamic element management
3. **Explore Different Sites**: Practice various automation scenarios
4. **Write Custom Tests**: Create your own test cases
5. **Advanced Patterns**: API testing, visual testing, performance

---

**Perfect for Learning** 🎓 | **Safe Practice** 🛡️ | **Real Automation** 🎭
