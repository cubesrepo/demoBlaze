import pytest

from pages.signup_page import SignupPage


@pytest.mark.signup
class TestSignupPage:
    @pytest.fixture
    def signup_page(self, driver, delay):
        return SignupPage(driver, delay)

    def test_valid_signup(self, signup_page):
        current_result_message, username, password = signup_page.verif_valid_signup()
        expected_result_message = "Sign up successful."

        assert current_result_message == expected_result_message, \
            f"Expected result to be {expected_result_message}, but got {current_result_message} instead."

    def test_signup_with_no_username_password(self, signup_page):
        current_alert_message = signup_page.verif_signup_with_no_username_password()

        expected_alert_message = "Please fill out Username and Password."

        assert current_alert_message == expected_alert_message, \
            f"Expected result to be {expected_alert_message}, but got {current_alert_message} instead."

    def test_login_with_no_existing_user(self, signup_page):
        current_alert_message = signup_page.verify_signup_with_existing_user()

        expected_alert_message = "This user already exist."

        assert current_alert_message == expected_alert_message, \
            f"Expected result to be {expected_alert_message}, but got {current_alert_message} instead."






