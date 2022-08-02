import time

from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):

    def setup(self):
        self.register_email = f"UserNameN{str(time.time())[-4:]}@fakemail.org"
        self.register_password = "1234Qwerty!"
        self.should_be_login_url()
        self.should_be_LOGIN_FORM_BUTTON()
        self.should_be_REGISTER_FORM_BUTTON()
        self.register_new_user(self.register_email, self.register_password)
        self.should_be_authorized_user()

    def go_to_logout(self):
        login_link = self.browser.find_element(*MainPageLocators.MAIN_LOGOUT_LINK)
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_LOGIN_FORM_BUTTON()
        self.should_be_REGISTER_FORM_BUTTON()

    def should_be_login_url(self):
        assert self.is_text_present_in_url(
            'login'), F"driver.current_url={self.browser.current_url} not contain 'login' "
        assert True

    def should_be_LOGIN_FORM_BUTTON(self):
        assert self.wait_is_element_present(*LoginPageLocators.LOGIN_FORM_BUTTON), "Login form is not presented"

    def should_be_REGISTER_FORM_BUTTON(self):
        assert self.wait_is_element_present(*LoginPageLocators.REGISTER_FORM_BUTTON), "Register form is not presented"

    def register_new_user(self, email, password):
        assert self.wait_is_element_present(
            *LoginPageLocators.REGISTER_EMAIL), "REGISTER_EMAIL element is not presented"
        self.set_text_for_element(*LoginPageLocators.REGISTER_EMAIL,
                                  email), f"value {email} not insert in REGISTER_EMAIL element"
        assert self.wait_is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD), "REGISTER_PASSWORD element is not presented"
        self.set_text_for_element(*LoginPageLocators.REGISTER_PASSWORD,
                                  password), f"value {password} not insert in REGISTER_PASSWORD element"
        assert self.wait_is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD2), "REGISTER_PASSWORD2 element is not presented"
        self.set_text_for_element(*LoginPageLocators.REGISTER_PASSWORD2,
                                  password), f"value {password} not insert in REGISTER_PASSWORD2 element"
        assert self.is_element_click(
            *LoginPageLocators.REGISTER_FORM_BUTTON), "REGISTER_FORM_BUTTON link is not clicked"
        time.sleep(4)
        error = self.wait_is_element_present(*LoginPageLocators.REGISTER_ERROR_BLOK)
        print(f"{error=}")
        if error:
            if self.wait_for_mask_in_element_attribute_text(LoginPageLocators.REGISTER_ERROR_BLOK,
                                                            "A user with that email address already exists"):
                self.login_exist_user(self, email, password)

    def login_exist_user(self, email, password):
        assert self.wait_is_element_present(
            *LoginPageLocators.LOGIN_EMAIL), "LOGIN_EMAIL element is not presented"
        self.set_text_for_element(*LoginPageLocators.LOGIN_EMAIL,
                                  email), f"value {email} not insert in REGISTER_EMAIL element"
        assert self.wait_is_element_present(
            *LoginPageLocators.LOGIN_PASSWORD), "LOGIN_PASSWORD element is not presented"
        self.set_text_for_element(*LoginPageLocators.LOGIN_PASSWORD,
                                  password), f"value {password} not insert in LOGIN_PASSWORD element"
        assert self.is_element_click(
            *LoginPageLocators.LOGIN_FORM_BUTTON), "LOGIN_FORM_BUTTON link is not clicked"
