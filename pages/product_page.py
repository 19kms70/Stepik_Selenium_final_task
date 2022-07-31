from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    # def should_be_product_page(self):
    #     self.should_be_product_url()
    #     self.should_be_btn_add_to_basket()
    #     self.should_be_btn_add_to_basket_clicked()
    #     self.solve_quiz_and_get_code()
    #     self.should_be_register_form()
    #     self.solve_quiz_and_get_code()

    def should_be_product_url(self):
        assert self.is_text_present_in_url('?promo=newYea'), F"driver.current_url={self.browser.current_url} not contain 'product' "
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_btn_add_to_basket(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "BTN_ADD_TO_BASKET is not presented"



    def should_be_btn_add_to_basket_clicked(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_click(*ProductPageLocators.BTN_ADD_TO_BASKET), "BTN_ADD_TO_BASKET is not clicked"

    def get_product_name(self):
        name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME)
        assert len(name) > 0, "product name is not presented"
        return name
    def get_product_name_approved(self):
        name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME_APPROVED)
        assert len(name) > 0, "product name is not presented"
        return name

    def get_product_price(self):
        name = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
        assert len(name) > 0, "product name is not presented"
        return name
    def get_product_price_approced(self):
        name = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE_APPROVED)
        assert len(name) > 0, "product name is not presented"
        return name
    def check_product_hase_been_added_to_bascek(self):
        message = self.get_element_text(*ProductPageLocators.PRODUCT_HASE_BEEN_ADDED_TO_BASKET)
        assert "has been added to your basket." in message , f"{message=} != 'has been added to your basket.'"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_HASE_BEEN_ADDED_TO_BASKET), \
            "Message about product has been added to your basket is presented, but should not be"
