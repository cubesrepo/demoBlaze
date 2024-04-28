import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage


class HomePage(BasePage):
    def verify_add_to_cart_all_phones_product(self):
        time.sleep(2)
        #SCROLL DOWN
        self.scroll_by_amount(0, 150)
        for phone in range(1, 8):
            #CLICK PHONE CATEGORY
            phone_category = self.wait_clickable(test_data.homepage.PHONES_CATEGORY, 15)
            self.action_click(phone_category)

            time.sleep(1)

            #PHONE XPATH TO CLICK
            phone_id = By.XPATH, f"//a[@href='prod.html?idp_={phone}']"
            phone_click = self.wait_visibility(phone_id, 15)

            #get the phone name to click
            phonename = self.get_text(phone_id, 5)

            time.sleep(0.5)

            #PHONE ARTICLE TO SCROLL TO.
            phone_articale = By.XPATH, f"(//p[@id='article'])[{phone}]"
            phone_arti = self.wait_presence(phone_articale, 15)
            self.scroll_to_element(phone_arti)
            time.sleep(0.5)

            #click the phone
            try:
                self.action_click(phone_click)
            except StaleElementReferenceException:
                phone_click = self.wait_clickable(phone_id, 15)

                phone_click.click()

            time.sleep(0.5)

            #get phone title
            phonetitle = self.get_text(test_data.homepage.PRODUCT_NAME_H2, 15)

            #assertion if phonename in phone title
            assert phonename in phonetitle

            time.sleep(0.5)

            #click addtocart btn
            addto_cart_btn = self.wait_clickable(test_data.homepage.ADD_TO_CART_BTN, 15)
            self.action_click(addto_cart_btn)

            time.sleep(1)
            # get the text of alert message
            alertmessage = self.get_alert_text()
            assert "Product added." in alertmessage

            self.alert_accept()

            time.sleep(0.5)

            home_menu = self.wait_clickable(test_data.homepage.HOME_MENU, 10)
            self.action_click(home_menu)

            time.sleep(0.5)




