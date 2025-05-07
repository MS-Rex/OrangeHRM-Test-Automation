from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    """Page object for dashboard page after successful login"""
    
    # Locators
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    MY_LEAVE_ICON = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a")
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-tab")
    LOGOUT_OPTION = (By.XPATH, "//a[text()='Logout']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_logged_in(self):
        """Check if user is logged in"""
        return self.is_dashboard_loaded()
    
    def is_dashboard_loaded(self):
        """Check if dashboard page is loaded by verifying header"""
        return self.is_displayed(self.DASHBOARD_HEADER)
    
    def click_my_leave(self):
        """Click on Leave icon in quick launch"""
        self.click(self.MY_LEAVE_ICON)
        from pages.leave_page import LeavePage
        return LeavePage(self.driver)
    
    def logout(self):
        """Perform logout"""
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_OPTION)
        from pages.login_page import LoginPage
        return LoginPage(self.driver)
