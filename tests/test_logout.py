from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLogout:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        # Login steps
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()

    def test_logout_functionality(self):
        # Open menu and click logout
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(1)
        assert "saucedemo.com" in self.driver.current_url
        assert "login" in self.driver.current_url

    def test_logout_visibility(self):
        # Open menu
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        # Check if logout link is visible
        logout = self.driver.find_element(By.ID, "logout_sidebar_link")
        assert logout.is_displayed()
