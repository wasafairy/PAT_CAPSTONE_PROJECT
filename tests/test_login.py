import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.parametrize("username", [
        "standard_user",
        "problem_user",
        "performance_glitch_user",
        "locked_out_user"
    ])
    def test_login_with_users(self, username):
        login = LoginPage(self.driver)
        login.login(username, "secret_sauce")

        print(f"URL after login for {username}: {self.driver.current_url}")

        if username == "locked_out_user":
            assert "sorry, this user has been locked out" in self.driver.page_source.lower()
        else:
            assert "inventory" in self.driver.current_url
