import time

from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

LINK = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_basket(browser):
    link = LINK
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_url()
    product_page.should_be_btn_add_to_basket()
    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()
    print(f"{product_price=}  {product_name=}")
    product_page.should_be_btn_add_to_basket_clicked()
    product_page.solve_quiz_and_get_code()
    product_name_approved = product_page.get_product_name_approved()
    product_price_approved = product_page.get_product_price_approced()
    print(f"{product_price_approved=}  {product_name_approved=}")
    assert product_name == product_name_approved, f"{product_name=} != {product_name_approved=}"
    assert product_price == product_price_approved, f"{product_price=} != {product_price_approved=}"
    product_page.check_product_hase_been_added_to_bascek()




