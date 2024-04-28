import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from tests.base_test import BaseTest

@pytest.mark.order(3)
class TesthomePage(BaseTest):
    def test_add_to_cart_all_phones_product_and_delete_in_cart(self, driver):
        homepage = HomePage(driver)
        cartpage = CartPage(driver)
        homepage.verify_add_to_cart_all_phones_product()
        cartpage.verify_delete_all_products_in_cart()

