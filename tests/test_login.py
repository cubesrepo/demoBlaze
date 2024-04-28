import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest

@pytest.mark.order(2)
class TestLogin(BaseTest):

    def test_login_without_username_and_password(self, driver):
        loginpage = LoginPage(driver)
        loginpage.verify_login_without_username_and_password()
    @pytest.mark.skip
    def test_login_without_username(self, driver):
        loginpage = LoginPage(driver)
        loginpage.verify_login_without_username()

    @pytest.mark.skip
    def test_login_without_password(self, driver):
        loginpage = LoginPage(driver)
        loginpage.verify_login_without_password()

    @pytest.mark.skip
    def test_login_with_wrong_password(self, driver):
        loginpage = LoginPage(driver)
        loginpage.verify_login_with_wrong_password()

    def test_login_with_valid_credentials(self, driver):
        loginpage = LoginPage(driver)
        loginpage.verify_login_with_valid_credentials()


