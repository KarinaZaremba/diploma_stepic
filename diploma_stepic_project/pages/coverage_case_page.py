from diploma_stepic_project.pages.base_page import BasePage


class CaseMobilePage(BasePage):

    """""Локаторы"""
    COLOR_CASE_LOCATOR = "//div[@style='background: #f6c2b7;']"
    ADD_TO_ORDER_LOCATOR = "//button[@id = 'add-to-cart-button-14593']"
    OPEN_CART_PAGE_LOCATOR = "//div[@class= 'h_basket_price']"
    FOR_MODEL_LOCATOR = "//*[text() = '  Samsung Galaxy S21 FE']"

    def choose_new_color(self):
        self.click(self.COLOR_CASE_LOCATOR)

    def open_cart_page(self):
        self.click(self.OPEN_CART_PAGE_LOCATOR)

    def get_name_case_for_model_phone(self):
        return self.get_element_text(self.FOR_MODEL_LOCATOR)

