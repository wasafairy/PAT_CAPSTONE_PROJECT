from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(self.driver, 10)

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located(self.username_input)).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

        self.driver.find_element(*self.login_button).click()

        # Wait for either successful login or error to show
        try:
            self.wait.until(EC.url_contains("inventory"))
        except:
            # Optional: Save a screenshot for debugging failed login
            self.driver.save_screenshot(f"screenshots/login_failed_{username}.png")
