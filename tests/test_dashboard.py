from pages.login_page import LoginPage
from utils.config import Config


class TestDashboard:
    """Test suite for Dashboard functionality"""

    def test_login_and_verify_dashboard(self, driver):
        """Test login functionality and verify dashboard is loaded"""
        # Arrange
        login_page = LoginPage(driver)

        # Act
        dashboard_page = login_page.open().login(Config.USERNAME, Config.PASSWORD)

        # Assert
        assert (
            dashboard_page.is_dashboard_loaded()
        ), "Dashboard page not loaded after login"

    def test_navigate_to_my_leave(self, driver):
        """Test navigating to My Leave page from dashboard"""
        # Arrange
        login_page = LoginPage(driver)
        dashboard_page = login_page.open().login(Config.USERNAME, Config.PASSWORD)

        # Act
        leave_page = dashboard_page.click_my_leave()

        # Assert
        assert (
            leave_page.is_leave_page_loaded()
        ), "Leave page not loaded after clicking My Leave"

        # Additional verifications for Leave page
        assert leave_page.is_displayed(
            leave_page.LEAVE_LIST
        ), "Leave List section not displayed"

    def test_logout(self, driver):
        """Test logout functionality"""
        # Arrange
        login_page = LoginPage(driver)
        dashboard_page = login_page.open().login(Config.USERNAME, Config.PASSWORD)

        # Act
        login_page = dashboard_page.logout()

        # Assert
        assert (
            login_page.is_login_page_loaded()
        ), "Not redirected to login page after logout"
