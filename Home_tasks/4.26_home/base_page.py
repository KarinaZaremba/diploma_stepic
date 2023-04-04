import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    """"по умолчанию будем обращаться к драйверу"""
    def __init__(self, driver):
        self.driver = driver

    """"определяю тип локатора. Работаю только с XPATH"""
    def _define_locator_type(self, locator):
        if "//" in locator:
            return By.XPATH

    def url_open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def _find_element(self, locator, timeout=10):
        return self.wait_for_element_presence(locator, timeout)

    def wait_for_element_presence(self, locator, time=10):
        locator_type = self._define_locator_type(locator)
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((locator_type, locator)))
        return element

    def click(self, locator):
        element = self._find_element(locator)
        element.click()

    def get_element_text(self, locator):
        element = self._find_element(locator)
        return element.text

    def send_text(self, locator, text):
        element = self._find_element(locator)
        element.send_keys(text)

    def add_to_cart(self, locator):
        element = self._find_element(locator)
        element.click()

    def clear(self, locator):
        element = self._find_element(locator)
        element.clear()

    def refresh_page(self):
        self.driver.refresh()

    def get_details(self, name1_locator1, add_cart_locator2, get_element_locator_3):
        name = self.get_element_text(name1_locator1)
        print(f'{name} - Добавлен в корзину')
        self.click(add_cart_locator2)
        self.url_open("https://www.saucedemo.com/cart.html")
        name1 = self.get_element_text(get_element_locator_3)
        assert name == name1
        print("Assert прошел успешно")
        self.click('//*[@id="checkout"]')
        time.sleep(2)
