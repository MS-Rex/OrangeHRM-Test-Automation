# OrangeHRM Test Automation Framework

![Run Selenium Tests](https://github.com/MS-Rex/OrangeHRM-Test-Automation/actions/workflows/test.yml/badge.svg)

A fully workflow supported test automation framework for OrangeHRM using Selenium WebDriver with Python, implementing the Page Object Model design pattern.

## Features

- **Page Object Model Architecture**: Clear separation between test logic and page interactions
- **Configurable Environment**: Support for multiple environments via .env file
- **HTML Test Reports**: Detailed reports with test results and screenshots
- **CI/CD Integration**: GitHub Actions workflow for automated test execution
- **Secure Credential Management**: Environment variables for sensitive information

## Project Structure

```
selenium_pom_framework/
│
├── pages/                  # Page Objects layer
│   ├── __init__.py
│   ├── base_page.py        # Base page with common methods
│   ├── login_page.py       # Login page implementation
│   ├── dashboard_page.py   # Dashboard page implementation
│   └── leave_page.py       # Leave page implementation
│
├── tests/                  # Test Layer
│   ├── __init__.py
│   ├── conftest.py         # PyTest configuration & fixtures
│   ├── test_login.py       # Login tests
│   └── test_dashboard.py   # Dashboard and functional tests
│
├── utils/                  # Utilities
│   ├── __init__.py
│   ├── driver_factory.py   # WebDriver factory
│   └── config.py           # Configuration management
│
├── .github/
│   └── workflows/
│       └── test.yml        # GitHub Actions workflow
│
├── .env.example            # Example environment variables
├── .python-version         # Python version specification
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

## Prerequisites

- Python (version specified in `.python-version`)
- uv package manager
- Chrome browser

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/OrangeHRM-test-automation.git
   cd OrangeHRM-test-automation
   ```

2. Set up Python environment (if using pyenv):

   ```bash
   pyenv install $(cat .python-version)  # If not already installed
   pyenv local $(cat .python-version)
   ```

3. Install dependencies using uv:
   ```bash
   uv pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file from the example:

   ```bash
   cp .env.example .env
   ```

2. Update the `.env` file with your OrangeHRM credentials:
   ```
   ORANGEHRM_USERNAME=your_username
   ORANGEHRM_PASSWORD=your_password
   ORANGEHRM_URL=https://opensource-demo.orangehrmlive.com/
   HEADLESS=False
   ```

## Running Tests

### Run all tests:

```bash
uv run pytest
```

### Run with HTML report:

```bash
uv run pytest --html=reports/report.html --self-contained-html
```

### Run specific test file:

```bash
uv run pytest tests/test_login.py
```

### Run tests with specific browser:

```bash
uv run pytest --browser=chrome
```

### Accessing Reports

You can access the HTML test reports in several ways:

1. **Direct Link** (works when viewing repo locally):

   ```
   [View Latest Test Report](./reports/report.html)
   ```

2. **HTML Preview** (works on GitHub):
   ```
   [View Latest Test Report](https://htmlpreview.github.io/?https://github.com/MS-Rex/OrangeHRM-Test-Automation/tree/main/main/reports/report.html)
   ```

## CI/CD Integration

This project includes a GitHub Actions workflow that:

- Automatically runs tests on pull requests to main/develop branches
- Sets up the correct Python version from `.python-version`
- Uses uv for package management
- Runs tests in headless mode
- Generates and uploads HTML test reports as artifacts

## Test Examples

### Login Test

```python
def test_successful_login(self, driver):
    """Test successful login with valid credentials"""
    login_page = LoginPage(driver)
    dashboard_page = login_page.open().login(Config.USERNAME, Config.PASSWORD)
    assert dashboard_page.is_dashboard_loaded()
```

### Navigation Test

```python
def test_navigate_to_my_leave(self, driver):
    """Test navigating to My Leave page from dashboard"""
    login_page = LoginPage(driver)
    dashboard_page = login_page.open().login(Config.USERNAME, Config.PASSWORD)
    leave_page = dashboard_page.click_my_leave()
    assert leave_page.is_leave_page_loaded()
```

## Key Framework Principles

1. **Separation of Concerns**: Test logic is separate from page implementation
2. **Reusability**: Common actions are defined once in BasePage
3. **Method Chaining**: Fluent interface for better readability
4. **Explicit Waits**: Built-in waits for handling dynamic content
5. **Environment Flexibility**: Tests can run in different environments with minimal changes

## Author

Miyuru Sanjana

## License

This project is licensed under the MIT License - see the LICENSE file for details.
