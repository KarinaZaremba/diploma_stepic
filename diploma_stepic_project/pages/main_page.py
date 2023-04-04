from diploma_stepic_project.pages.base_page import BasePage


class MainPage(BasePage):
    """""Локаторы для навигации и перключения языка"""
    URL = "https://zoommer.ge/"
    LANGUAGE_MENU_LOCATOR = "//div[@class = 'content_div']//a[@class='h_language_selected']"
    RUSSIAN_LANGUAGE_LOCATOR = "//div[@class = 'header_top_div']//a[@title='RUSSIAN']"

    """""Локаторы для входа в личный кабинет"""
    PROFILE_BUTTON_LOCATOR = "//div[@class='user_profile']"

    email = "zarembawork@yandex.ru"
    password = "1qazxsw2"

    EMAIL_LOCATOR = "//input[@name= 'EmailOrPhone']"
    PASSWORD_LOCATOR = "//input[@id= 'Password']"
    LOGIN_BUTTON_LOCATOR = "//button[@id= 'login-btn']"

    """""Поисковые локаторы"""
    SEARCH_AREA_LOCATOR = "//input[@id='small-searchterms']"
    SEARCh_button_locator = '//*[@id="small-search-box-form"]/button'

    def navigate(self):
        self.url_open(self.URL)

    def change_language(self):
        self.select_menu(self.LANGUAGE_MENU_LOCATOR, self.RUSSIAN_LANGUAGE_LOCATOR)
        self.refresh_page()

    def open_profile_info(self):
        self.click(self.PROFILE_BUTTON_LOCATOR)

    def input_email(self):
        self.send_text(self.EMAIL_LOCATOR, self.email)

    def input_password(self):
        self.send_text(self.PASSWORD_LOCATOR, self.password)

    def input_product_name(self):
        self.input_product(self.SEARCH_AREA_LOCATOR, "Samsung Galaxy S21 FE 5G")

    def main_page_steps(self):
        self.navigate()
        self.change_language()
        self.open_profile_info()
        self.input_email()
        self.input_password()
        self.click(self.LOGIN_BUTTON_LOCATOR)
        self.refresh_page()
        self.input_product_name()
