from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

def open_page(browser, link):
    print(f"Testing link={link}")
    page = MainPage(browser,
                    link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    return page

class MainPage(BasePage):
    """
     The class MainPage describes the main methods for working on main pages
    """
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.MAIN_LOGIN_LINK)
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.MAIN_LOGIN_LINK), "Login link is not presented"

