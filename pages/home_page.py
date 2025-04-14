from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.logout_link).click()

    def is_logout_visible(self):
        self.driver.find_element(*self.menu_button).click()
        return self.driver.find_element(*self.logout_link).is_displayed()

    def is_cart_visible(self):
        return self.driver.find_element(*self.cart_icon).is_displayed()
