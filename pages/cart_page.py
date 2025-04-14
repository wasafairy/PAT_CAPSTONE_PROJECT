from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def get_cart_product_details(self):
        items = self.driver.find_elements(*self.cart_items)
        details = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            details.append({"name": name, "price": price})
        return details
