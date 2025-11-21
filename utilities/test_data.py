from selenium.webdriver.common.by import By

BASE_URL = "https://www.demoblaze.com/"

USERNAME = "notexist"
PASSWORD = "mation123123"


class login:
    LOGIN_MENU = By.XPATH, "//a[@data-target='#logInModal']"
    USERNAME = By.XPATH, "//input[@id='loginusername']"
    PASSWORD = By.XPATH, "//input[@id='loginpassword']"
    LOGITN_BTN = By.XPATH, "//button[@onclick='logIn()']"

class homepage:
    LOG_OUT = By.XPATH, "//a[@id='logout2']"
    WELCOME_USER = By.XPATH, "//a[@id='nameofuser']"

    PHONES_CATEGORY = By.XPATH, "//div[@id='contcont']//a[2]"

    PRODUCT_NAME_H2 = By.XPATH, "//h2[@class='name']"
    ADD_TO_CART_BTN = By.XPATH, f"//a[text()='Add to cart']"
    HOME_MENU = By.XPATH, "//a[@href='index.html']"
    CART_MENU = By.XPATH, "//a[@href='cart.html']"


class register:
    REGISTER_MENU = By.XPATH, "//a[@data-target='#signInModal']"
    USERNAME = By.XPATH, "//input[@id='sign-username']"
    PASSWORD = By.XPATH, "//input[@id='sign-password']"
    SIGNUP_BTN = By.XPATH, "//button[@onclick='register()']"


class cart:
    PLACE_ORDER = By.XPATH, "//button[text()='Place Order']"

    NAME = By.XPATH, "//input[@id='name']"
    COUNTRY = By.XPATH, "//input[@id='country']"
    CITY = By.XPATH, "//input[@id='city']"
    CREDIT_CARD = By.XPATH,"//input[@id='card']"
    MONTH = By.XPATH,"//input[@id='month']"
    YEAR = By.XPATH,"//input[@id='year']"
    PURCHASE = By.XPATH, "//button[@onclick='purchaseOrder()']"

    THANKYOU_PURCHASE_TEXT = By.XPATH, "//h2[text()='Thank you for your purchase!']"
    SUMMARY = By.XPATH, "//p[@class='lead text-muted ']"
    OK_BTN = By.XPATH, "//button[text()='OK']"

    TOTAL_HEADER = By.XPATH, "//h3[@id='totalp']"
    TOTAL_ITEM = By.XPATH, "(//tr[@class='success'])[1]/td[3]"

    SAMSUNG_S6 = By.XPATH, "(//a[normalize-space()='Samsung galaxy s6'])[1]"
    NOKIA = By.XPATH, "//a[normalize-space()='Nokia lumia 1520']"
    NEXUS = By.XPATH, "//a[normalize-space()='Nexus 6']"
    SAMSUNG_S7= By.XPATH, "//a[normalize-space()='Samsung galaxy s7']"
    IPHONE6 = By.XPATH, "//a[normalize-space()='Iphone 6 32gb']"
    SONY = By.XPATH, "//a[normalize-space()='Sony xperia z5']"

    ADD_TO_CART_BTN = By.XPATH, "//a[normalize-space()='Add to cart']"
    TOTAL = By.XPATH, "//h3[@id='totalp']"








