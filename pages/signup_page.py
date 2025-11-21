import time

from faker import Faker

from pages.base_page import BasePage
from utilities import test_data


class SignupPage(BasePage):
    def click_signup_menu(self):
        self.wait_clickable(test_data.register.REGISTER_MENU).click()
    def click_signup_btn(self):
        self.wait_clickable(test_data.register.SIGNUP_BTN).click()
    def get_welcome_name(self):
        return self.get_text(test_data.homepage.WELCOME_USER).strip()

    def enter_username_password(self, username, password):
        self.type(test_data.register.USERNAME, username)
        self.type(test_data.register.PASSWORD, password)

    def verif_valid_signup(self):
        fake = Faker()

        self.click_signup_menu()
        username = f"tes_username{fake.email()}"
        password = "123123531243"
        self.enter_username_password(username, password)
        self.click_signup_btn()

        current_result_message = self.get_alert_message()
        self.wait_and_accept_alert()
        return current_result_message, username, password

    def verif_signup_with_no_username_password(self):
        self.click_signup_menu()
        self.click_signup_btn()

        current_result_message = self.get_alert_message()
        self.wait_and_accept_alert()
        return current_result_message

    def verify_signup_with_existing_user(self):
        self.click_signup_menu()
        self.enter_username_password(test_data.USERNAME, test_data.PASSWORD)
        self.click_signup_btn()

        current_alert_message = self.get_alert_message()
        self.wait_and_accept_alert()
        time.sleep(1)
        return current_alert_message






