from base_page import BasePage


class Check(BasePage):

    FIRST_NAME_LOCATOR = '//*[@id="first-name"]'
    LAST_NAME_LOCATOR = '//*[@id="last-name"]'
    ZIP_LOCATOR = '//*[@id="postal-code"]'
    BUTTON_LOCATOR = '//*[@id="continue"]'
    PRICE_LOCATOR = '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div'
    ITEM_TOTAL_PRICE = '//*[@id="checkout_summary_container"]/div/div[2]/div[5]'
    FINISH_BUTTON = '//*[@id="finish"]'

    def input_personal_data(self):
        self.send_text(self.FIRST_NAME_LOCATOR, "Karina")
        self.send_text(self.LAST_NAME_LOCATOR, "Karina")
        self.send_text(self.ZIP_LOCATOR, "123456")

    def click_continue(self):
        self.click(self.BUTTON_LOCATOR)

    def compare_prices(self):
        price = self.get_element_text(self.PRICE_LOCATOR)
        new_price = str(price).replace('$', '')
        print(f'Прайс - {price}')
        item_price = self.get_element_text(self.ITEM_TOTAL_PRICE)
        new_item_price = str(item_price).replace('Item total: $', '')
        print(f'Прайс_2 - {item_price}')

        assert new_price == new_item_price
        print(f"Цена соответсвует. Завершаем БП - {new_price} = {new_item_price}")

    def click_finish_button(self):
        self.click(self.FINISH_BUTTON)