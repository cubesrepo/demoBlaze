import time

import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from tests.base_test import BaseTest

@pytest.mark.order(4)
class TestcartPage(BaseTest):

    def test_place_order_functionality(self, driver):
        homepage = HomePage(driver)
        cartpage = CartPage(driver)
        homepage.verify_add_to_cart_all_phones_product()
        cartpage.verify_place_order_functionality()