import pytest
import allure
from selenium.webdriver.common.by import By
from pages.order_scooter import OrderScooter
from curl import home_page, page_dzen
import data

from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
import data
import time

class TestOrderScooter:
    @allure.title("Тест успешного заказа самоката")
    def test_success_ful_order(self, driver):
        order_scooter = OrderScooter(driver)
        order_scooter.click_order_button()
        order_scooter.fill_first_order_form("Петр", 'Петров', 'Лубянка', '89098887766')
        time.sleep(10)
        order_scooter.click_metro_button('Луб')
        #order_scooter.click_order_button()
        time.sleep(10)