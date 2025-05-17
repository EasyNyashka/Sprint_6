from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
import data
from data import OrderScooterFirst
import allure


class OrderScooter(BasePage):
    @allure.step("Нажать кнопку Заказа")
    def click_order_button(self):
        self.click_on_element(HomePageLocators.ORDER_BUTTON_TOP)

    @allure.step("Заполнить первую страницу формы")
    def fill_first_order_form(self, name, surname, address, telephone):
        self.send_keys_to_input(OrderPageLocators.NAME, name)
        self.send_keys_to_input(OrderPageLocators.SURNAME, surname)
        self.send_keys_to_input(OrderPageLocators.ADDRESS, address)
        self.send_keys_to_input(OrderPageLocators.TELEPHONE, telephone)

    @allure.step("Выбор станции метро")
    def click_metro_button(self, metro):
        self.click_on_element(OrderPageLocators.BUTTON_METRO)
        self.send_keys_to_input(OrderPageLocators.BUTTON_METRO_ENTER, metro)



    #@allure.step("Нажать кнопку Далее")
    #def click_order_button(self):
        #self.click_on_element(OrderPageLocators.BUTTON_NEXT)