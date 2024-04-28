import pytest

from pages.signup_page import SignUpPage
from tests.base_test import BaseTest
@pytest.mark.skip
#@pytest.mark.order(1)
class TestsignupPage(BaseTest):


    def test_signup_with_existing_account(self, driver):
        signuppage = SignUpPage(driver)
        signuppage.verify_register_with_existing_account()

    def test_signup_with_valid_username_and_password(self, driver):
        signuppage = SignUpPage(driver)
        signuppage.verify_register_with_valid_username_and_password()