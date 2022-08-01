from .base_page import BasePage
from .locators import BusketPageLocators

BASKET_EMPTY_MESSAGE = 'basket is empty'
BASKET_ITEMS_TO_BY_NOW = 'items to by now'

class BusketPage(BasePage):
    """
     The class BusketPage describes the main methods for working on busket pages
    """

    def see_message_basket_is_empty(self, mask):
        assert self.wait_for_mask_in_element_attribute_text(BusketPageLocators.BASKET_CONTENT, mask), f"Do not see message: {mask}"

    def do_not_see_message_item_to_by_now(self, mask):
        assert self.wait_for_mask_not_in_element_attribute_text(BusketPageLocators.BASKET_CONTENT, mask), f"see message: {mask}"

    def not_see_message_item_to_by_now(self):
        assert self.is_not_element_present(*BusketPageLocators.ITEMS_TO_BY_NOW), \
            "See element for ITEMS_TO_BY_NOW"
