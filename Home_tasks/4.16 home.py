from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

MAIN_PAGE_LOCATOR = 'https://www.saucedemo.com/'

driver = webdriver.Chrome(ChromeDriverManager().install())

""""проходим авторизацию на сайте"""
driver.get(MAIN_PAGE_LOCATOR)
driver.maximize_window()
enter_login = driver.find_element(By.XPATH, "//input[@id='user-name']")
enter_login.send_keys("standard_user")
enter_password = driver.find_element(By.XPATH, "//input[@id='password']")
enter_password.send_keys("secret_sauce")
button = driver.find_element(By.XPATH, "//input[@id='login-button']")
button.click()


"""Информация по первому товару. Сохраняем данные в переменные: продукт/цена/кнопка"""
first_product = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
name_first_product = first_product.text
print(f'Я выбрала первый продукт -  {name_first_product}')

second_product_price = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']/preceding-sibling::div")
value_first_product = second_product_price.text
print(f'Посмотрела на цену - {value_first_product}')

add_first_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
add_first_product.click()
print(f"Добавила в корзину")

""""Информация по второму товару. Сохраняем данные в переменные: продукт/цена/кнопка"""
second_product = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
name_second_product = second_product.text
print(f'Затем выбрала второй товар - {name_second_product}')

second_product_price = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']/preceding-sibling::div")
value_second_product = second_product_price.text
print(f'Посмотрела на цену - {value_second_product}')

add_second_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
add_second_product.click()
print("Тоже добавила в корзину")

""""нажимаем на корзину, берем информацию о товарах в ней и сохраняем в переменные"""
basket = driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']")
basket.click()

""""Первый товар в корзине. Проверяем название"""
first_product_cart = driver.find_element(By.XPATH, "//a[@id ='item_4_title_link']")
value_first_cart = first_product_cart.text
print(f'На всякий проверила в корзине первый товар - {value_first_cart}')

assert name_first_product == value_first_cart
print("Тест сказал, что все хорошо, тот товар")

price_first_product_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_first_cart = price_first_product_cart.text
print(f'и проверила цену первого {value_price_first_cart}')

assert value_first_product == value_price_first_cart
print("Тест сказал, что все хорошо, тот цена та")
##########################################################################
""""Второй товар в корзине"""
second_product_cart = driver.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div')
value_second_cart = second_product_cart.text
print(f'Обязательно сверила название второго товара - {value_second_product}')

assert name_second_product == value_second_cart
print("Тест подтвердил что все отлично. Имена одинаковые.")

price_second_product_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_second_cart = price_second_product_cart.text
print(f'И проверила цену второго, а то мало ли {value_price_first_cart}')

assert value_second_product == value_price_second_cart
print("Все значения сошлись")

checkout_botton = driver.find_element(By.XPATH, '//*[@id="checkout"]')
checkout_botton.click()
print("На радостях жму на кнопку")
############################################################################
""""заполнение полей для оформления заказа"""
first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
first_name.send_keys('Karina')
last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
last_name.send_keys('Karina')
zip = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
zip.send_keys('4444')
continue_botton =driver.find_element(By.XPATH, '//*[@id="continue"]')
continue_botton.click()
print("Ввела личные данные")

##########################################################################
""""оформление заказа"""
"""ФИНАЛ по первому и второсу товару. Проверяем цены"""

first_product_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_first_product = first_product_price.text
final_value_first_product = value_first_product.replace('$', '')
final_value_first_product = float(final_value_first_product)
print(f'Проверила цену окончательно - {final_value_first_product}')

second_product_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_second_product = second_product_price.text
final_value_second_product = value_second_product.replace('$', '')
final_value_second_product = float(final_value_second_product)
print(f'Проверила цену второго товара  - {final_value_second_product}')

total_price = final_value_first_product+final_value_second_product
print(f'На всякий сложила две цены: {value_first_product} + {value_second_product} = {total_price}')

""""Сверяем с тоталом корзины"""
default_total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]')
value_default_total = default_total.text
print(value_default_total)
final_default_total = value_default_total.replace('Item total: $', '')
final_default_total = float(final_default_total)
print(f'Проверила сумму по умолчанию - {final_default_total}')

assert total_price == final_default_total
print(f'Надо учиться доверять. Тест прошел успешно. Цены совпадают.')
