import pytest

from pages.login_page import LoginPage
from utilities import test_data


@pytest.mark.login
class TestLogin:
    @pytest.fixture
    def login_page(self, driver, delay):
        return LoginPage(driver, delay)

    def test_valid_login(self, login_page):
        current_user_login = login_page.verify_valid_login(test_data.USERNAME, test_data.PASSWORD)

        expected_user_login = f"Welcome {test_data.USERNAME}"

        assert  current_user_login == expected_user_login, \
            f"Expected result to be {expected_user_login}, but got {current_user_login} instead."

    def test_login_with_no_username_password(self, login_page):
        current_alert_message = login_page.verify_login_with_no_username_password()

        expected_alert_message = "Please fill out Username and Password."

        assert  current_alert_message == expected_alert_message, \
            f"Expected result to be {expected_alert_message}, but got {current_alert_message} instead."

    @pytest.mark.skip
    def test_login_with_no_existing_user(self, login_page):
        current_alert_message = login_page.verify_login_with_no_existing_user()

        expected_alert_message = "User does not exist."

        assert current_alert_message == expected_alert_message, \
            f"Expected result to be {expected_alert_message}, but got {current_alert_message} instead."









