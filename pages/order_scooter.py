import allure
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import time


class OrderScooter(BasePage):
    @allure.step("Нажать верхнюю кнопку Заказа")
    def click_order_button_top(self):
        self.click_on_element(HomePageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать нижнюю кнопку Заказа")
    def click_order_button_lower(self):
        self.click_on_element(HomePageLocators.COOKIE)
        self.wait_for_element(HomePageLocators.ORDER_BUTTON_LOWER)
        time.sleep(10)
        self.scroll_to_element(HomePageLocators.ORDER_BUTTON_LOWER)
        self.click_on_element(HomePageLocators.ORDER_BUTTON_LOWER)

    @allure.step("Заполнить первую страницу формы: имя, фамилия, адрес, телефон")
    def fill_first_order_form(self, name, surname, address, telephone):
        self.send_keys_to_input(OrderPageLocators.NAME, name)
        self.send_keys_to_input(OrderPageLocators.SURNAME, surname)
        self.send_keys_to_input(OrderPageLocators.ADDRESS, address)
        self.send_keys_to_input(OrderPageLocators.TELEPHONE, telephone)

    @allure.step("Выбор станции метро")
    def choose_metro(self, station_name):
        self.click_on_element(OrderPageLocators.BUTTON_METRO)
        self.send_keys_to_input(OrderPageLocators.BUTTON_METRO, station_name)
        self.click_on_element(OrderPageLocators.BUTTON_METRO_ENTER)

    @allure.step("Нажать кнопку Далее")
    def click_button_further(self):
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Заполнить вторую страницу формы: дата, срок аренды")
    def fill_second_order_form(self, date, comment):
        self.send_keys_to_input(OrderPageLocators.WHEN_TO_BRING, date)
        self.send_keys_to_input(OrderPageLocators.COMMENT, comment)

    @allure.step("Выбор, когда привезти самокат")
    def choose_rental_period(self):
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.NUMBER_OF_DAYS)

    @allure.step("Выбор цвета самоката")
    def choose_scooter_color(self):
        self.click_on_element(OrderPageLocators.SCOOTER_COLOR)

    @allure.step("Нажать кнопку Заказать")
    def click_button_order(self):
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step("Подтвердить заказ")
    def click_button_yes(self):
        self.click_on_element(OrderPageLocators.PLACE_AN_ORDER)

    @allure.step("Посмотреть статус")
    def click_button_view_status(self):
        self.click_on_element(OrderPageLocators.VIEW_STATUS)

    @allure.step("Проверить, что заказ создан")
    def check_number_order(self):
        number = self.get_text_on_element(OrderPageLocators.ORDER_CHECK)
        return number