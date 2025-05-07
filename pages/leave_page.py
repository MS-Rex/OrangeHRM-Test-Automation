from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LeavePage(BasePage):
    """Page object for Leave page"""

    # Locators
    LEAVE_HEADER = (By.XPATH, "//h6[text()='Leave']")
    LEAVE_LIST = (By.XPATH, "//h5[text()='Leave List']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_leave_page_loaded(self):
        """Check if Leave page is loaded by verifying header"""
        header_displayed = self.is_displayed(self.LEAVE_HEADER)
        list_displayed = self.is_displayed(self.LEAVE_LIST)
        return list_displayed and header_displayed
