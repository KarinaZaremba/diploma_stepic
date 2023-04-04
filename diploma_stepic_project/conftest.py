import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from diploma_stepic_project.pages.main_page import MainPage
from diploma_stepic_project.pages.coverage_case_page import CaseMobilePage
from diploma_stepic_project.pages.search_page import SearchPage


@pytest.fixture()
def set_up_mobile_products(chromedriver, main_page, search_page):
    main_page.main_page_steps()
    search_page.choose_mobile()
    search_page.choose_mobile_color()

    yield
    chromedriver.quit()


@pytest.fixture()
def chromedriver():
    s = Service('C:\\Users\\Karina\\.wdm\\drivers\\chromedriver\\win32\\111.0.5563.64\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    return driver


@pytest.fixture()
def main_page(chromedriver):
    return MainPage(chromedriver)


@pytest.fixture()
def search_page(chromedriver):
    return SearchPage(chromedriver)


@pytest.fixture()
def coverage_case_page(chromedriver):
    return CaseMobilePage(chromedriver)


@pytest.fixture()
def cart_page(chromedriver):
    return CartPage(chromedriver)