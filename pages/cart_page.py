import time

from faker import Faker
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities import test_data


class CartPage(BasePage):
    def click_add_to_cart_btn(self):
        self.wait_clickable(test_data.cart.ADD_TO_CART_BTN).click()
    def click_home(self):
        self.wait_clickable(test_data.homepage.HOME_MENU).click()
    def click_cart(self):
        self.wait_clickable(test_data.homepage.CART_MENU).click()
    def get_total(self):
        text = self.get_text(test_data.cart.TOTAL).strip()
        return text
    def click_place_order(self):
        self.wait_clickable(test_data.cart.PLACE_ORDER).click()
    def click_delete_btn(self):
        while True:
            delete = By.XPATH, f"(//a[@href='#'][normalize-space()='Delete'])[1]"
            if self.wait_visibility(delete) is None:
                break
            self.wait_clickable(delete).click()
            time.sleep(0.5)
    def type_info(self, name, country, city, credit_card, month, year):
        info_details = {
            test_data.cart.NAME: name,
            test_data.cart.COUNTRY: country,
            test_data.cart.CITY: city,
            test_data.cart.CREDIT_CARD: credit_card,
            test_data.cart.MONTH: month,
            test_data.cart.YEAR: year
        }
        for locator, value in info_details.items():
            self.type(locator, value)
    def click_purchase(self):
        self.wait_clickable(test_data.cart.PURCHASE).click()
    def add_to_cart_product(self):
        products = [
            test_data.cart.SAMSUNG_S6,
            test_data.cart.NOKIA,
            test_data.cart.NEXUS,
            test_data.cart.SAMSUNG_S7,
            test_data.cart.IPHONE6,
            test_data.cart.SONY
        ]
        for product in products:
            self.wait_clickable(product).click()

            self.click_add_to_cart_btn()

            # ALWAYS wait for the alert here
            alert_text = self.wait_and_accept_alert()
            self.logger.info(f"Alert handled: {alert_text}")

            self.click_home()

    def verify_valid_add_to_cart(self):
        self.add_to_cart_product()
        self.click_cart()
        current_total = self.get_total()
        expected_total = "3740"

        return current_total, expected_total

    def verify_place_order_with_valid_info(self):
        self.add_to_cart_product()
        self.click_cart()

        self.click_place_order()
        fake = Faker()
        self.type_info(fake.first_name(), fake.country(), fake.city(), "123", "March", "2025")
        self.click_purchase()

        current_result_thankyou_message = self.get_text(test_data.cart.THANKYOU_PURCHASE_TEXT)
        expected_result_thankyou_message = "Thank you for your purchase!"
        return current_result_thankyou_message, expected_result_thankyou_message

    def verify_place_order_without_info(self):
        self.add_to_cart_product()
        self.click_cart()

        self.click_place_order()
        fake = Faker()

        self.click_purchase()

        current_message = self.wait_and_accept_alert()
        expected_message = "Please fill out Name and Creditcard."

        return current_message, expected_message

    def verify_place_order_after_deleting_products(self):
        self.add_to_cart_product()
        self.click_cart()
        self.click_delete_btn()

        self.click_place_order()
        fake = Faker()
        self.type_info(fake.first_name(), fake.country(), fake.city(), "123", "March", "2025")
        self.click_purchase()

        current_result_thankyou_message = self.get_text(test_data.cart.THANKYOU_PURCHASE_TEXT)
        expected_result_thankyou_message = "Thank you for your purchase!"
        return current_result_thankyou_message, expected_result_thankyou_message



