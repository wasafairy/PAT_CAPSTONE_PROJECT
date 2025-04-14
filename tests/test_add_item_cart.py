import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_add_4_random_products_to_cart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

    # Get all product items
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) == 6, f"Expected 6 products, found {len(products)}"

    # Select 4 random products
    selected = random.sample(products, 4)

    print("\nSelected Products:")
    for product in selected:
        name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"{name} - {price}")
        product.find_element(By.TAG_NAME, "button").click()
        time.sleep(0.3)

    # Check cart badge
    try:
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_badge == '4', f"Expected 4 items in cart, found {cart_badge}"
    except NoSuchElementException:
        assert False, "Cart badge not found — possibly no items were added"

    driver.quit()
