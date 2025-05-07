from pages.login_page import LoginPage

class TestLogin:
    """Test suite for login functionality"""
    
    def test_login_page_title(self, driver):
        """Test login page title"""
        # Arrange
        login_page = LoginPage(driver)
        
        # Act
        login_page.open()
        
        # Assert
        assert "OrangeHRM" in driver.title, "Login page title is incorrect"

    def test_successful_login(self, driver):
        """Test successful login with valid credentials"""
        # Arrange
        login_page = LoginPage(driver)
        
        # Act
        dashboard_page = login_page.open().login("Admin", "admin123")
    
    def test_invalid_credentials(self, driver):
        """Test login failure with invalid credentials"""
        # Arrange
        login_page = LoginPage(driver)
        
        # Act
        login_page.open().login("WrongAdmin", "Wrongadmin123")
        
        # Assert
        assert login_page.is_error_displayed(), "Error message not displayed"
        assert "Invalid credentials" in login_page.get_error_message(), "Incorrect error message"
    
    def test_empty_username(self, driver):
        """Test login with empty username"""
        # Arrange
        login_page = LoginPage(driver)
        
        # Act
        login_page.open().login("","any_password")
        
        # Assert
        assert login_page.is_username_validation_message_displayed(), "Username validation message not displayed"
        assert "Required" in login_page.get_username_validation_message(), "Incorrect username validation message"
    
    def test_empty_password(self, driver):
        """Test login with empty password"""
        # Arrange
        login_page = LoginPage(driver)
        
        # Act
        login_page.open().login("any_username", "")
        
        # Assert
        assert login_page.is_password_validation_message_displayed(), "Password validation message not displayed"
        assert "Required" in login_page.get_password_validation_message(), "Incorrect password validation message"
