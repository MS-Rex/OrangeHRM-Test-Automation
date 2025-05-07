from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """Base class for all page objects with common methods"""
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20 # Had to increase the timeout to 20 seconds to avoid timeout errors
    
    def visit(self, url):
        """Navigate to the specified URL"""
        self.driver.get(url)
    
    def find_element(self, locator):
        """Find an element with wait"""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise Exception(f"Element not found with locator: {locator}")
    
    def click(self, locator):
        """Click on an element"""
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    def input_text(self, locator, text):
        """Input text into an element"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text from an element"""
        element = self.find_element(locator)
        return element.text
    
    def is_displayed(self, locator):
        """Check if element is visible"""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
