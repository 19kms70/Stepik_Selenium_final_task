from selenium.webdriver.common.by import By


class MainPageLocators():
    MAIN_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_link")
    MAIN_OPEN_BASKET = (By.XPATH, "//a[@class='btn btn-default']")


class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#login_form input[type='email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#login_form input[type='password']")
    LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, "[value='Log In']")
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, "[value='Register']")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#register_form input[type='email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#register_form input[type='password']")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    REGISTER_ERROR_BLOK = (By.CLASS_NAME, "error-block")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page  h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_page h1 + p.price_color")
    PRODUCT_NAME_APPROVED = (By.CSS_SELECTOR, "#messages div div strong")
    PRODUCT_PRICE_APPROVED = (By.CSS_SELECTOR, ".product_page h1 + p.price_color")
    PRODUCT_HASE_BEEN_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages div div")


class BasketPageLocators():
    BASKET_CONTENT = (By.XPATH, "//*[@id='content_inner']/p")
    ITEMS_TO_BY_NOW = (By.XPATH, "//*[@id='content_inner']/div[1]/div/h2")


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    MAIN_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_link")
    MAIN_OPEN_BASKET = (By.XPATH, "//a[@class='btn btn-default']")
