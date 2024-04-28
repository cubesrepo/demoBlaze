import time

from faker import Faker
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage


class CartPage(BasePage):

    def verify_place_order_functionality(self):
        time.sleep(2)
        cart_menu = self.wait_clickable(test_data.homepage.CART_MENU, 10)
        self.action_click(cart_menu)

        time.sleep(1)

        cart_btn = self.wait_clickable(test_data.cart.PLACE_ORDER, 15)
        self.action_click(cart_btn)

        time.sleep(0.5)
        fake = Faker()

        #Input name
        namevalue = fake.first_name()
        self.send_keys(10, test_data.cart.NAME, namevalue)
        time.sleep(0.5)

        # Input country
        countryvalue = "Canada"
        self.send_keys(10, test_data.cart.COUNTRY, countryvalue)
        time.sleep(0.5)


        # Input city
        cityvalue = "City"
        self.send_keys(10, test_data.cart.CITY, cityvalue)
        time.sleep(0.5)

        self.scroll_by_amount(0, 60)

        # Input credit
        creditvalue = "123124234"
        self.send_keys(10, test_data.cart.CREDIT_CARD, creditvalue)
        time.sleep(0.5)

        # Input month
        monthvalue = "DECEMBER"
        self.send_keys(10, test_data.cart.MONTH, monthvalue)
        time.sleep(0.5)

        # Input year
        yearvalue = "2025"
        self.send_keys(10, test_data.cart.YEAR, yearvalue)
        time.sleep(0.5)

        #click purchase btm
        purchase = self.wait_clickable(test_data.cart.PURCHASE, 15)
        self.action_click(purchase)

        time.sleep(1)

        #check the thankou text is display
        assert self.wait_visibility(test_data.cart.THANKYOU_PURCHASE_TEXT, 10)

        time.sleep(0.5)

        #click ok btn
        ok_Btn = self.wait_clickable(test_data.cart.OK_BTN, 10)
        self.action_click(ok_Btn)

    def verify_delete_all_products_in_cart(self):
        time.sleep(2)
        cart_menu = self.wait_clickable(test_data.homepage.CART_MENU, 10)
        self.action_click(cart_menu)

        time.sleep(1)

        while True:
            delbtn = By.XPATH, f"(//a[@href='#'][normalize-space()='Delete'])[1]"
            try:
                total_header = self.get_text(test_data.cart.TOTAL_HEADER, 10)
                total_item = self.get_text(test_data.cart.TOTAL_ITEM, 10)

                delete_btn = self.wait_clickable(delbtn, 10)
            except TimeoutException:
                break

            if delete_btn:
                time.sleep(0.5)

                self.action_click(delete_btn)
                time.sleep(1)
                subtract_total = int(total_header) - int(total_item)

                print(subtract_total)

                time.sleep(1)

            else:
                assert not total_header, "Total header still displayed"

                break

        home = self.wait_clickable(test_data.homepage.HOME_MENU, 10)
        self.action_click(home)

