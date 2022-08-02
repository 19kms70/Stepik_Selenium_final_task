import time
import pytest

from .pages.basket_page import *
from .pages.main_page import *
from .pages.login_page import LoginPage

LINK="http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = LINK
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        time.sleep(3)
        login_page.should_be_login_page()
        time.sleep(3)

    def test_guest_should_see_login_link(self, browser):
        link = LINK
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link=LINK
    page =MainPage(browser, link)
    page.open()
    page.click_to_view_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.do_not_see_message_item_to_by_now(BASKET_ITEMS_TO_BY_NOW)
    basket_page.see_message_basket_is_empty(BASKET_EMPTY_MESSAGE)