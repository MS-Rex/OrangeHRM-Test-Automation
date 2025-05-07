from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config import Config

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
            if Config.HEADLESS:
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--window-size=1920,1080")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.maximize_window()
        return driver
