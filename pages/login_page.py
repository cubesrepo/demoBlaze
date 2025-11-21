import time

from pages.base_page import BasePage
from utilities import test_data


class LoginPage(BasePage):
    def click_login_menu(self):
        self.wait_clickable(test_data.login.LOGIN_MENU).click()
    def click_login_btn(self):
        self.wait_clickable(test_data.login.LOGITN_BTN).click()
    def get_welcome_name(self):
        return self.get_text(test_data.homepage.WELCOME_USER).strip()

    def enter_username_password(self, username, password):
        self.type(test_data.login.USERNAME, username)
        self.type(test_data.login.PASSWORD, password)

    def verify_valid_login(self, username, password):
        self.click_login_menu()
        self.enter_username_password(username, password)
        self.click_login_btn()

        current_user_login = self.get_welcome_name()

        return current_user_login

    def verify_login_with_no_username_password(self):
        self.click_login_menu()
        self.click_login_btn()

        current_alert_message = self.get_alert_message()
        time.sleep(1)

        return current_alert_message

    def verify_login_with_no_existing_user(self):
        self.click_login_menu()
        self.enter_username_password("usern55123ist1234", "pass123")
        self.click_login_btn()

        current_alert_message = self.get_alert_message()
        time.sleep(1)
        return current_alert_message








