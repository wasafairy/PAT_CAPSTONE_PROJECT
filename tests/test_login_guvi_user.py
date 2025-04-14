import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestGuviUserLogin:

    def test_guvi_user_login(self):
        login = LoginPage(self.driver)
        login.login("guvi_user", "Secret@123")

        # Assertion to check if login was successful
        assert "inventory" in self.driver.current_url, "Login failed for guvi_user"
