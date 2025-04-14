from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_all_items_to_cart(self):
        buttons = self.driver.find_elements(*self.add_to_cart_buttons)
        for button in buttons:
            button.click()

    def click_cart_button(self):
        self.driver.find_element(*self.cart_button).click()
