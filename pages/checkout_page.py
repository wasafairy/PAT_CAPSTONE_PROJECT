from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.overview_items = (By.CLASS_NAME, "cart_item")
        self.confirmation_text = (By.CLASS_NAME, "complete-header")

    def fill_user_info(self, first, last, postal):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(postal)
        self.driver.find_element(*self.continue_button).click()

    def get_overview_product_details(self):
        items = self.driver.find_elements(*self.overview_items)
        details = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            details.append({"name": name, "price": price})
        return details

    def finish_checkout(self):
        self.driver.find_element(*self.finish_button).click()

    def get_confirmation(self):
        return self.driver.find_element(*self.confirmation_text).text
