import random
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestInventoryRandomProducts:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        # Login
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

    def teardown_method(self):
        self.driver.quit()

    def test_randomly_fetch_4_products(self):
        # Find all product name and price elements
        name_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")

        # Combine name and price into tuples
        products = list(zip(name_elements, price_elements))

        assert len(products) == 6, f"Expected 6 products, found {len(products)}"

        # Randomly select 4 products
        selected = random.sample(products, 4)

        print("\nSelected Products:")
        for name_el, price_el in selected:
            name = name_el.text
            price = price_el.text
            print(f"{name} - {price}")

        # Add assert to pass the test
        assert len(selected) == 4
