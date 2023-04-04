
from registration_page import Registration
from catalog_page import CatalogPage
from check_out_step import Check
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:\\Users\\Karina\\.wdm\\drivers\\chromedriver\\win32\\109.0.5414.74\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
registration = Registration(driver)
registration.open_page()
registration.enter_login()
registration.enter_password()
registration.confirm()
catalog_page = CatalogPage(driver)
catalog_page.show_info()
catalog_page.show_details()
catalog_page.choose_a_product()
check_out_page = Check(driver)
check_out_page.input_personal_data()
check_out_page.click_continue()
check_out_page.compare_prices()
check_out_page.click_finish_button()


