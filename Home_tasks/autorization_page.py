from base_page import BasePage
from selenium.common.exceptions import TimeoutException


class Autorization(BasePage):

    MAIN_PAGE_LOCATOR = 'https://www.saucedemo.com/'
    LOGIN_AREA_LOCATOR = '//*[@id="user-name"]'
    PASSWORD_AREA_LOCATOR = '//*[@id="password"]'
    password = 'secret_sauce'
    LOGIN_BUTTON_LOCATOR = '//input[@id="login-button"]'
    BURGER_MENU_LOCATOR = "//button[@id = 'react-burger-menu-btn']"
    LOGOUT_LOCATOR = "//a[@id = 'logout_sidebar_link']"
    PRODUCT_LOGO = '//*[@id="header_container"]/div[2]/span'
    LOCKED_LOCATOR = '//*[@id="login_button_container"]/div/form/div[3]/h3'
    ERROR_BUTTON_MAIN_PAGE = "//button[@class = 'error-button']"
    MAIN_PAGE_TEXT_LOCATOR = '//*[@id="login_credentials"]/h4'

    def navigate(self):
        self.url_open(self.MAIN_PAGE_LOCATOR)

    def check_data(self):
        login_data = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
        for login in login_data:
            self.autorization(self.LOGIN_AREA_LOCATOR, login, self.PASSWORD_AREA_LOCATOR,
                              self.password, self.LOGIN_BUTTON_LOCATOR)
            if login in login_data:
                # self.autorization(self.LOGIN_AREA_LOCATOR, login, self.PASSWORD_AREA_LOCATOR,
                #                   self.password, self.LOGIN_BUTTON_LOCATOR)
                logo = self.get_element_text(self.PRODUCT_LOGO)
                print('взяли текст лого')
                assert logo == "PRODUCTS"
                print("Assert с standard_user и problem_user прошел успешно")
                self.select_burger_menu(self.BURGER_MENU_LOCATOR, self.LOGOUT_LOCATOR)
                print("Выбрали бургер и вышли")
            if login in login_data:
                print("Новая авторизация")
                self.autorization(self.LOGIN_AREA_LOCATOR, login, self.PASSWORD_AREA_LOCATOR,
                                  self.password, self.LOGIN_BUTTON_LOCATOR)
                print("Берем текст")
                text = self.get_element_text(self.LOCKED_LOCATOR_ERROR_TEXT)
                assert text == "Epic sadface: Sorry, this user has been locked out."
                self.click(self.ERROR_BUTTON_MAIN_PAGE)
                print('Assert с locked_out_user прошел успешно. Мы остались на главной')
        print("вот и конец")