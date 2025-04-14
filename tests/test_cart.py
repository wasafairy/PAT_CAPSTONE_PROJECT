import pytest
from pages.login_page import LoginPage
from pages.inventory_page import HomePage
from pages.cart_page import CartPage

@pytest.mark.usefixtures("setup")
class TestCart:

    def test_cart_product_details(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        home = HomePage(driver)
        home.add_all_items_to_cart()
        home.click_cart_button()

        cart = CartPage(driver)
        products = cart.get_cart_product_details()

        # Print product details for debugging
        for product in products:
            print(f"Product Name: {product['name']}, Price: {product['price']}")

        assert len(products) > 0, "No products found in the cart"
