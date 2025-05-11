from selenium.webdriver.common.by import By

class HomePageLocators:

    # Логотип Яндекс
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # Логотип Самокат
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    # Кнопка заказа верхняя
    ORDER_BUTTON_TOP = (By.XPATH, "//div[@class='Header_Nav__AGCXC'] and //button[contains(@class, 'Button_Button__ra12g')")

    # Кнопка заказа нижняя
    ORDER_BUTTON_LOWER = (By.XPATH, "//button[@class='Button_Middle__1CSJM']")

    # Вопрос
    QUESTION = (By.ID, 'accordion__heading-{}')

    # Ответ
    ANSWER = (By.ID, 'accordion__panel-{}')

