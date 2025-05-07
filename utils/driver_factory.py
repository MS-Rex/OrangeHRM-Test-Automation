from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:
    """Factory for creating WebDriver instances"""

    @staticmethod
    def get_driver(browser="chrome"):
        """
        Get WebDriver instance based on browser name

        Args:
            browser (str): Browser name (currently only implemented chrome support)

        Returns:
            WebDriver: Configured WebDriver instance
        """
        browser = browser.lower()

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.maximize_window()
        return driver
