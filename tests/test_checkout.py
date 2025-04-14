import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import HomePage
from pages.cart_page import CartPage

@pytest.mark.usefixtures("setup")
class TestCheckoutFlow:

    def login(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

    def add_products_to_cart(self):
        home = HomePage(self.driver)
        home.add_all_items_to_cart()
        home.click_cart_button()

    def go_to_cart_and_checkout(self):
        # Wait for the cart page to load and checkout button to appear
        wait = WebDriverWait(self.driver, 10)
        checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_btn.click()

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def finish_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "finish"))
        ).click()

    def test_checkout_process(self):
        self.login()
        self.add_products_to_cart()
        self.go_to_cart_and_checkout()
        self.fill_checkout_info("John", "Doe", "12345")
        self.finish_checkout()

        # Assert checkout success message
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text

        assert success_message == "Thank you for your order!", "Checkout failed!"
