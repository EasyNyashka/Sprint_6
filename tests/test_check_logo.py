import allure

from pages.check_logo import CheckLogoScooter, CheckLogoYandex
from curl import *

class TestCheckLogoScooter:
    @allure.step("Тест проверки логотипа Самокат")
    def test_check_logo_scooter(self, driver):
        check_logo = CheckLogoScooter(driver)
        check_logo.click_order_button_top()
        check_logo.click_order_button_scooter()
        check_logo.check_current_url_is_home_page(home_page)

    @allure.step("Тест проверки логотипа Яндекс")
    def test_check_logo_yandex(self, driver):
        check_logo = CheckLogoYandex(driver)
        check_logo.click_order_button_scooter()
        check_logo.check_current_url_is_home_page(page_dzen)

