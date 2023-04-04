from diploma_stepic_project.pages.base_page import BasePage


class SearchPage(BasePage):

    MOBILE_LOCATOR = "//div[@id = 'product_image_slider_id_13428']/a[@data-prd-id = '13428']"
    COOKIES_LOCATOR = '//*[@id="close-btn"]'

    """""Детали телефона"""
    COLOR_MOBILE_LOCATOR = "//div[@id='product_attribute_15001_226349']/child::div"
    TEXT_COLOR_LOCATOR = "//strong[text()='Lavender']"
    ADD_ORDER_LOCATOR = "//button[@id='add-to-cart-button-13427']"

    """""Аксессуары к телефону"""
    SCROLL_LOCATOR = "//div[@class='title_left_side']/h2[text()='Аксессуары']"
    CHECKBOX_LOCATOR = "//div[@class='product-gallery-filter']/descendant::label[1]"
    CASE_LOCATOR = "//div[contains(text(), 'Coverage Silicon Case Samsung Galaxy S21 FE Peach')]"

    def choose_mobile(self):
        self.click(self.MOBILE_LOCATOR)

    def choose_mobile_color(self):
        self.click(self.COLOR_MOBILE_LOCATOR)

    def get_color_text(self):
        return self.get_element_text(self.TEXT_COLOR_LOCATOR)

    def add_mobile_to_cart(self):
        self.click(self.ADD_ORDER_LOCATOR)

    def scroll_to_case(self):
        self.scroll_down()

    def click_checkbox(self):
        self.click(self.CHECKBOX_LOCATOR)
        self.click(self.CASE_LOCATOR)

    def search_page_steps(self):
        self.choose_mobile()
        self.choose_mobile_color()
        self.add_mobile_to_cart()
        self.scroll_to_case()
        self.click_checkbox()

