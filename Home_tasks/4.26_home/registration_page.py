from base_page import BasePage


class Registration(BasePage):

    URL = "https://www.saucedemo.com/"
    LOGIN_AREA = '//*[@id="user-name"]'
    login = "standard_user"
    PASSWORD_AREA = '//*[@id="password"]'
    password = "secret_sauce"
    LOGIN_BUTTON = '//*[@id="login-button"]'
    text = "Приветствую в магазине!"

    def open_page(self):
        self.url_open(self.URL)

    def enter_login(self):
        self.send_text(self.LOGIN_AREA, self.login)

    def enter_password(self):
        self.send_text(self.PASSWORD_AREA, self.password)

    def confirm(self):
        self.click(self.LOGIN_BUTTON)



