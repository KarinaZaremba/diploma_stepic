from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import keyboard


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _define_locator_type(self, locator):
        if "//" in locator:
            return By.XPATH

    def url_open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def close_driver(self):
        self.driver.quit()

    def _find_element(self, locator, timeout=30):
        return self.wait_for_element_presence(locator, timeout)

    def wait_for_element_presence(self, locator, timeout=30):
        locator_type = self._define_locator_type(locator)
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((locator_type, locator)))
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

    def clear(self, locator):
        element = self._find_element(locator)
        element.clear()

    def refresh_page(self):
        self.driver.refresh()

    def select_menu(self, menu_locator, language_locator):
        menu = self.wait_for_element_presence(menu_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(menu).perform()
        language = self._find_element(language_locator)
        language.click()

    def input_product(self, area_locator, text):
        area = self._find_element(area_locator)
        area.click()
        keyboard.write(text)
        keyboard.send("enter")

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 400);")

