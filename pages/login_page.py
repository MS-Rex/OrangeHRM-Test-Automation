from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page object for login page"""
    
    #XPATHs for elements
    btn_login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button' # XPATH for Login button
    error_message_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p' # XPATH for Error message
    username_validation_message_xpath= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span' # XPATH for Username Validation message
    password_validation_message_xpath= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span' # XPATH for Password Validation message
    
    # Locators
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, btn_login_xpath)
    ERROR_MESSAGE = (By.XPATH, error_message_xpath)
    USERNAME_VALIDATION_MESSAGE = (By.XPATH, username_validation_message_xpath)
    PASSWORD_VALIDATION_MESSAGE = (By.XPATH, password_validation_message_xpath)

    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    def open(self):
        """Open the login page"""
        self.visit(self.url)
        return self
    
    def enter_username(self, username):
        """Enter username in the username field"""
        self.input_text(self.USERNAME_FIELD, username)
        return self
    
    def enter_password(self, password):
        """Enter password in the password field"""
        self.input_text(self.PASSWORD_FIELD, password)
        return self
    
    def login(self, username, password):
        """Perform full login flow"""
        self.enter_username(username)
        self.enter_password(password)
        return self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """Get login error message text"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """Check if error message is displayed"""
        return self.is_displayed(self.ERROR_MESSAGE)
    
    def get_username_validation_message(self):
        """Get username validation message text"""
        return self.get_text(self.USERNAME_VALIDATION_MESSAGE)
    
    def is_username_validation_message_displayed(self):
        """Check if validation message is displayed"""
        return self.is_displayed(self.USERNAME_VALIDATION_MESSAGE)
    
    def get_password_validation_message(self):
        """Get password validation message text"""
        return self.get_text(self.PASSWORD_VALIDATION_MESSAGE)

    def is_password_validation_message_displayed(self):
        """Check if validation message is displayed"""
        return self.is_displayed(self.PASSWORD_VALIDATION_MESSAGE)





