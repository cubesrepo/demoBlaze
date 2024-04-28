import random
import string
import time

import pytest

import test_data
from pages.base_page import BasePage

@pytest.mark.order(1)
class SignUpPage(BasePage):

    def verify_register_with_existing_account(self):
        time.sleep(2)
        #click sign up menu
        signupmenu = self.wait_clickable(test_data.register.REGISTER_MENU, 15)
        self.action_click(signupmenu)

        time.sleep(0.5)

        #input username
        self.send_keys(15, test_data.register.USERNAME, test_data.USERNAME)
        time.sleep(0.5)

        # input password
        self.send_keys(15, test_data.register.PASSWORD, test_data.PASSWORD)

        time.sleep(0.5)
        #click signup btn
        signup_btn = self.wait_clickable(test_data.register.SIGNUP_BTN, 15)
        self.action_click(signup_btn)
        time.sleep(0.5)

        # get the alert text and assert it
        text = self.get_alert_text()
        assert "This user already exist." in text
        time.sleep(0.5)

        self.alert_accept()

    def verify_register_with_valid_username_and_password(self):
        time.sleep(2)

        # input username
        usernamevalue = ''.join(random.choices(string.ascii_lowercase, k=6))
        username = self.wait_visibility(test_data.register.USERNAME, 15)
        self.action_send_keys_with_clear(username, usernamevalue)
        time.sleep(0.5)

        # input username
        passwordvalue = "123123"
        password = self.wait_visibility(test_data.register.PASSWORD, 15)
        self.action_send_keys_with_clear(password, passwordvalue)
        time.sleep(0.5)

        # click signup btn
        signup_btn = self.wait_clickable(test_data.register.SIGNUP_BTN, 15)
        self.action_click(signup_btn)
        time.sleep(0.5)

        # get the alert text and assert it
        text = self.get_alert_text()
        assert "Sign up successful." in text
        time.sleep(0.5)

        self.alert_accept()