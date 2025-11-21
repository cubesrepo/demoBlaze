import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


@pytest.mark.cart
class TestCart:

    @pytest.fixture
    def cart_page(self, driver, delay):
        return CartPage(driver, delay)
    @pytest.fixture
    def signup_page(self, driver, delay):
        return SignupPage(driver, delay)
    @pytest.fixture
    def login_page(self, driver, delay):
        return LoginPage(driver, delay)
    @pytest.mark.skip
    def test_valid_add_to_cart(self, signup_page, cart_page, login_page):
        current_result_message, username, password = signup_page.verif_valid_signup()
        current_user_login = login_page.verify_valid_login(username, password)

        current_total, expected_total = cart_page.verify_valid_add_to_cart()

        assert current_total == expected_total, \
            f"Expected result to be {expected_total}, but got {current_total} instead."
    @pytest.mark.skip
    def test_place_order_with_valid_info(self, signup_page, cart_page, login_page):
        current_result_message, username, password = signup_page.verif_valid_signup()
        current_user_login = login_page.verify_valid_login(username, password)

        current_result_thankyou_message, expected_result_thankyou_message = cart_page.verify_place_order_with_valid_info()

        assert current_result_thankyou_message == expected_result_thankyou_message, \
            f"Expected result to be {expected_result_thankyou_message}, but got {current_result_thankyou_message} instead."
    @pytest.mark.skip
    def test_place_order_without_info(self, signup_page, cart_page, login_page):
        current_result_message, username, password = signup_page.verif_valid_signup()
        current_user_login = login_page.verify_valid_login(username, password)

        current_message, expected_message = cart_page.verify_place_order_without_info()

        assert current_message == expected_message, \
            f"Expected result to be {expected_message}, but got {current_message} instead."

    def test_place_order_after_deleting_products(self, signup_page, cart_page, login_page):
        current_result_message, username, password = signup_page.verif_valid_signup()
        current_user_login = login_page.verify_valid_login(username, password)

        current_result_thankyou_message, expected_result_thankyou_message = cart_page.verify_place_order_after_deleting_products()

        assert current_result_thankyou_message == expected_result_thankyou_message, \
            f"Expected result to be {expected_result_thankyou_message}, but got {current_result_thankyou_message} instead."










