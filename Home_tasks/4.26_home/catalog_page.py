import time

from base_page import BasePage


class CatalogPage(BasePage):

    ADD_1_PRODUCT = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    ADD_2_PRODUCT = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    ADD_3_PRODUCT = '//*[@id="add-to-cart-sauce-labs-onesie"]'
    ADD_4_PRODUCT = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
    ADD_5_PRODUCT = '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'
    ADD_6_PRODUCT = '//*[@id="remove-test.allthethings()-t-shirt-(red)"]'
    URL_CART_PAGE = 'https://www.saucedemo.com/cart.html'
    URL_CATEGORY_PAGE = 'https://www.saucedemo.com/inventory.html'

    def show_info(self):
        print("Добро пожаловать на наш сайт!")

    def show_details(self):
        print("Выберите интересущий товар:"
              "1 - Sauce Labs Backpack; "
              "2 - Sauce Labs Bolt T-Shirt;"
              "3 - Sauce Labs Onesie; "
              "4 - Sauce Labs Bike Light;"
              "5 - Sauce Labs Fleece Jacket;"
              "6 - T-Shirt (Red).")

    def choose_a_product(self):
        product = int(input("Введите номер товара - "))
        if product == 1:
            self.get_details('//*[@id="item_4_title_link"]/div', self.ADD_1_PRODUCT,
                             '//*[@id="item_4_title_link"]/div')
        elif product == 2:
            self.get_details('//*[@id="item_1_title_link"]/div', self.ADD_2_PRODUCT,
                             '//*[@id="item_1_title_link"]/div')
        elif product == 3:
            self.get_details('//*[@id="item_2_title_link"]/div', self.ADD_3_PRODUCT,
                             '//*[@id="item_2_title_link"]/div')
        elif product == 4:
            self.get_details('//*[@id="item_0_title_link"]/div', self.ADD_4_PRODUCT,
                             '//*[@id="item_0_title_link"]/div')
        elif product == 5:
            self.get_details('//*[@id="item_5_title_link"]/div', self.ADD_5_PRODUCT,
                             '//*[@id="item_5_title_link"]/div')
        elif product == 6:
            self.get_details('//*[@id="item_3_title_link"]/div', self.ADD_6_PRODUCT,
                             '//*[@id="item_3_title_link"]/div')
        else:
            print("Данный продукт отсутствует")

