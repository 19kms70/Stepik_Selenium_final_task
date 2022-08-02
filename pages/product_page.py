from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """
     The class ProductPage describes the main methods for working on product pages
    """

    def add_product_to_basket_and_calculate(self):
        self.should_be_product_url()
        self.should_be_btn_add_to_basket()
        self.should_not_be_success_message()
        product_name = self.get_product_name()
        product_price = self.get_product_price()
        print(f"{product_price=}  {product_name=}")
        self.should_be_btn_add_to_basket_clicked()
        self.solve_quiz_and_get_code()
        product_name_approved = self.get_product_name_approved()
        product_price_approved = self.get_product_price_approced()
        print(f"{product_price_approved=}  {product_name_approved=}")
        assert product_name == product_name_approved, f"Product name in basket:{product_name_approved} but you select:{product_name}"
        assert product_price == product_price_approved, f"Price in basket:{product_price_approved} but you select:{product_price}"
        self.check_product_hase_been_added_to_bascek()

    def should_be_product_url(self):
        check_str = 'catalogue'
        assert self.is_text_present_in_url(
            check_str), F"driver.current_url={self.browser.current_url} not contain 'product' "
        assert True

    def should_be_btn_add_to_basket(self):
        assert self.wait_is_element_present(
            *ProductPageLocators.BTN_ADD_TO_BASKET), "BTN_ADD_TO_BASKET is not presented"

    def should_be_btn_add_to_basket_clicked(self):
        assert self.is_element_click(*ProductPageLocators.BTN_ADD_TO_BASKET), "BTN_ADD_TO_BASKET is not clicked"

    def get_product_name(self):
        name = self.get_element_attribute_text(*ProductPageLocators.PRODUCT_NAME)
        assert len(name) > 0, "product name is not presented"
        return name

    def get_product_name_approved(self):
        name = self.get_element_attribute_text(*ProductPageLocators.PRODUCT_NAME_APPROVED)
        assert len(name) > 0, "product name is not presented"
        return name

    def get_product_price(self):
        name = self.get_element_attribute_text(*ProductPageLocators.PRODUCT_PRICE)
        assert len(name) > 0, "product name is not presented"
        return name

    def get_product_price_approced(self):
        name = self.get_element_attribute_text(*ProductPageLocators.PRODUCT_PRICE_APPROVED)
        assert len(name) > 0, "product name is not presented"
        return name

    def check_product_hase_been_added_to_bascek(self):
        message = self.get_element_attribute_text(*ProductPageLocators.PRODUCT_HASE_BEEN_ADDED_TO_BASKET)
        assert "has been added to your basket." in message, f"{message=} != 'has been added to your basket.'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_HASE_BEEN_ADDED_TO_BASKET), \
            "Message about product has been added to your basket is presented, but should not be"

    def add_product_to_basket(self):
        self.should_be_product_url()
        self.should_be_btn_add_to_basket()
        self.should_not_be_success_message()
        product_name = self.get_product_name()
        product_price = self.get_product_price()
        print(f"{product_price=}  {product_name=}")
        self.should_be_btn_add_to_basket_clicked()
        self.solve_quiz_and_get_code()
        product_name_approved = self.get_product_name_approved()
        product_price_approved = self.get_product_price_approced()
        print(f"{product_price_approved=}  {product_name_approved=}")
        assert product_name == product_name_approved, f"Product name in basket:{product_name_approved} but you select:{product_name}"
        assert product_price == product_price_approved, f"Price in basket:{product_price_approved} but you select:{product_price}"
        self.check_product_hase_been_added_to_bascek()

    def is_disappered_message_about_adding_in_basket(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_HASE_BEEN_ADDED_TO_BASKET), "Wrong show success message"
