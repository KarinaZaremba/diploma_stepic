import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from autorization_page import Autorization


s = Service('C:\\Users\\Karina\\.wdm\\drivers\\chromedriver\\win32\\109.0.5414.74\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

autorization_page = Autorization(driver)
autorization_page.navigate()
autorization_page.check_data()
