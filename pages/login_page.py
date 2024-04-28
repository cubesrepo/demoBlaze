import time

import test_data
from pages.base_page import BasePage


class LoginPage(BasePage):

    def verify_login_without_username_and_password(self):
        time.sleep(2)

        #click login menu btn
        login_menu = self.wait_clickable(test_data.login.LOGIN_MENU, 15)
        self.action_click(login_menu)

        time.sleep(0.5)

        #click login btn
        login_btn = self.wait_clickable(test_data.login.LOGITN_BTN, 15)
        self.action_click(login_btn)

        time.sleep(0.5)
        # get the alert text and assert it
        text = self.get_alert_text()
        assert "Please fill out Username and Password." in text
        time.sleep(0.5)

        self.alert_accept()
    def verify_login_without_username(self):
        time.sleep(2)

        #INPUT PASSWORD
        self.send_keys(15, test_data.login.PASSWORD, test_data.PASSWORD)

        time.sleep(0.5)
        # click login btn
        login_btn = self.wait_clickable(test_data.login.LOGITN_BTN, 15)
        self.action_click(login_btn)

        time.sleep(0.5)
        # get the alert text and assert it
        text = self.get_alert_text()
        assert "Please fill out Username and Password." in text
        time.sleep(0.5)

        self.alert_accept()
    def verify_login_without_password(self):
        time.sleep(2)

        # INPUT username
        self.send_keys(15, test_data.login.USERNAME, test_data.USERNAME)

        #claer password
        password = self.wait_visibility(test_data.login.PASSWORD, 15)
        self.action_backspace(password)

        time.sleep(0.5)
        # click login btn
        login_btn = self.wait_clickable(test_data.login.LOGITN_BTN, 15)
        self.action_click(login_btn)

        time.sleep(0.5)
        # get the alert text and assert it
        text = self.get_alert_text()
        assert "Please fill out Username and Password." in text
        time.sleep(0.5)

        self.alert_accept()


    def verify_login_with_wrong_password(self):
        time.sleep(2)

        #input username
        time.sleep(0.5)
        username = self.wait_visibility(test_data.login.USERNAME, 15)
        self.action_send_keys_with_clear(username, test_data.USERNAME)
        time.sleep(0.5)

        #Input password
        password = self.wait_visibility(test_data.login.PASSWORD, 15)
        self.action_send_keys_with_clear(password, "wrongpass")

        time.sleep(0.5)
        # click login btn
        login_btn = self.wait_clickable(test_data.login.LOGITN_BTN, 15)
        self.action_click(login_btn)

        time.sleep(0.5)
        # get the alert text and assert it
        text = self.get_alert_text()
        assert "Wrong password." in text
        time.sleep(0.5)

        self.alert_accept()

    def verify_login_with_valid_credentials(self):
        time.sleep(2)

        #input username
        time.sleep(0.5)
        username = self.wait_visibility(test_data.login.USERNAME, 15)
        self.action_send_keys_with_clear(username, test_data.USERNAME)
        time.sleep(0.5)

        # input password
        password = self.wait_visibility(test_data.login.PASSWORD, 15)
        self.action_send_keys_with_clear(password,  test_data.PASSWORD)

        time.sleep(0.5)
        # click login btn
        login_btn = self.wait_clickable(test_data.login.LOGITN_BTN, 15)
        self.action_click(login_btn)

        time.sleep(0.5)

        assert self.wait_visibility(test_data.homepage.LOG_OUT, 5)
        assert self.wait_visibility(test_data.homepage.WELCOME_USER, 5)