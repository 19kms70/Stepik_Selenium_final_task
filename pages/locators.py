from selenium.webdriver.common.by import By


class MainPageLocators():
    MAIN_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_OPEN_BASKET = (By.XPATH, "//a[@class='btn btn-default']")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "[value='Log In']")
    REGISTER_FORM = (By.CSS_SELECTOR, "[value='Register']")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page  h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_page h1 + p.price_color")
    PRODUCT_NAME_APPROVED = (By.CSS_SELECTOR, "#messages div div strong")
    PRODUCT_PRICE_APPROVED = (By.CSS_SELECTOR, ".product_page h1 + p.price_color")
    PRODUCT_HASE_BEEN_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages div div")


class BusketPageLocators():
    BASKET_CONTENT = (By.XPATH, "//*[@id='content_inner']/p")
    ITEMS_TO_BY_NOW = (By.XPATH, "//*[@id='content_inner']/div[1]/div/h2")

