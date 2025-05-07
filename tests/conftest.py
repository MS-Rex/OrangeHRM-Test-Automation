import pytest
from utils.driver_factory import DriverFactory
from datetime import datetime

def pytest_addoption(parser):
    """Add command line options"""
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome", 
        help="Browser to run tests: chrome"
    )

@pytest.fixture(scope="function")
def driver(request):
    """
    WebDriver fixture for tests
    
    Returns:
        WebDriver: Configured browser instance
    """
    browser_name = request.config.getoption("--browser")
    driver = DriverFactory.get_driver(browser_name)
    
    # Yield driver to the test
    yield driver
    
    # Cleanup after test
    driver.quit()

# HTML Report configuration
def pytest_html_report_title(report):
    report.title = "OrangeHRM Test Report"

def pytest_configure(config):
     return [
        ("Test Run Timestamp", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Project", "OrangeHRM-test-automation"),
        ("Author", "Miyuru Sanjana"),
    ]

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"<p>Test Framework: Selenium Python POM</p>"])
