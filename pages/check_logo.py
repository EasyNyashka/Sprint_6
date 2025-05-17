import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class CheckLogoScooter(BasePage):
    @allure.step("Нажать верхнюю кнопку Заказа")
    def click_order_button_top(self):
        self.click_on_element(HomePageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать логин Самокат")
    def click_order_button_scooter(self):
        self.click_on_element(HomePageLocators.LOGO_SCOOTER)

    @allure.step("Проверить, что открылась главная страница Самоката")
    def check_current_url_is_home_page(self, home_url):
        current_url = self.driver.current_url
        assert current_url == home_url

class CheckLogoYandex(BasePage):
    @allure.step("Нажать логин Самокат")
    def click_order_button_scooter(self):
        self.click_on_element(HomePageLocators.LOGO_YANDEX)

    @allure.step("Проверить, что открылась главная страница Самоката")
    def check_current_url_is_home_page(self, home_url):
        current_url = self.driver.current_url
        return current_url == home_url
