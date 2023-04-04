import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import datetime
from datetime import timedelta
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://demoqa.com/date-picker')
driver.maximize_window()

""""Сначала определяю поле ввода даты, чтобы можно было к нему привязать datetime."""
current_data = driver.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]')

""""Зациклила команду, чтобы не было повторения строки current_data.send_keys(Keys.BACK_SPACE) * 10 раз. 
Много лишнего текста. Цель - удалить первичнчую дату. 
У меня current_data.clear() не сработало."""
n = 1
while True:
    current_data.click()
    current_data.send_keys(Keys.BACK_SPACE)
    n = n +1
    if n == 11:
        break
    print("OK")

""""Определяю текущую дату (today)"""
data_today = datetime.datetime.today()
print(f"Now - {data_today}")
new_date = data_today + timedelta(days=10)

""""Перевожу дату в нужный формат"""
new_date_1 = new_date.strftime('%m/%d/%Y')
final_date = str(new_date_1)
print(f"+10 days - {final_date}")
current_data.send_keys(final_date)
time.sleep(5)
