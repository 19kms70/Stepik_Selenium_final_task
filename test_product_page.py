import time

import pytest

from .pages.locators import ProductPageLocators
from .pages.main_page import *
from .pages.product_page import ProductPage
from .pages.basket_page import *
from .pages.login_page import LoginPage

# LINK_OLD1 = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# LINK_OLD2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# LINK_FOR_CLASS = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = MainPage(browser,link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.setup()
        yield
        login_page.go_to_logout()
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        print(f"Testing link={link}")
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket_and_calculate()
        #page.should_be_login_link()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


list_of_failed_num = [7]
LINK="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
tested_links = [f"{LINK}?promo=offer{i}" if i not in list_of_failed_num else
                pytest.param(f"{LINK}?promo=offer{i}",
                             marks=pytest.mark.xfail(reason="some bug", strict=True)
                             )
                for i in range(1)]


@pytest.mark.need_review
@pytest.mark.parametrize("link", tested_links)
def test_guest_can_add_product_to_basket(browser, link):
    print(f"Testing link={link}")
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket_and_calculate()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()
    # "If test not passed - it is ok"


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    assert product_page.is_disappeared(
        *ProductPageLocators.PRODUCT_HASE_BEEN_ADDED_TO_BASKET), "If test not passed - it is ok"


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_to_view_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.do_not_see_message_item_to_by_now(BASKET_ITEMS_TO_BY_NOW)
    basket_page.see_message_basket_is_empty(BASKET_EMPTY_MESSAGE)

