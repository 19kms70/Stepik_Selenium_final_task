import math

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import MainPageLocators, BasePageLocators


class BasePage():
    """
     The class BasePage describes the main methods for working on all pages
    """

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(5)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def get_element_attribute_text(self, how, what):
        return self.browser.find_element(how, what).text

    def wait_for_mask_in_element_attribute_text(self, how_what, mask, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(how_what, mask))
        except TimeoutException:
            return False
        return True

    def wait_for_mask_not_in_element_attribute_text(self, how_what, mask, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(how_what, mask))
        except TimeoutException:
            return True
        return False

    def is_element_click(self, how, what):
        try:
            self.browser.find_element(how, what).click()
        except (NoSuchElementException):
            return False
        return True

    def is_text_present_in_url(self, text):
        return text in self.browser.current_url

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def wait_is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def click_to_view_basket(self):
        assert self.wait_is_element_present(*MainPageLocators.MAIN_OPEN_BASKET), "Basket link is not presented"
        assert self.is_element_click(*MainPageLocators.MAIN_OPEN_BASKET), "Basket link is not clicked"

    def set_text_for_element(self, how, what, text):
        print(f"{how=}, {what=}, {text=}")
        element = self.browser.find_element(how, what)
        element.send_keys(text)
        return

    def should_be_authorized_user(self):
        assert self.wait_is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.wait_is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
