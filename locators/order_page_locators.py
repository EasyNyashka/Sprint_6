from selenium.webdriver.common.by import By

class OrderPageLocators:

    # Поле ввода Имя
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    # Поле ввода Фамилии
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Поле ввода адреса
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # поле ввода станции метро
    Input_Input__1iN_Z Track_Input__1g7lq Input_Responsible__1jDKN
    # Поле ввода телефона
    TELEPHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка Далее
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    # Поле ввода Когда привезти самокат
    WHEN_TO_BRING = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # Поле ввода Срок аренды
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-root is-open']")
    # Выпадающий список
    NUMBER_OF_DAYS = (By.XPATH, "//div[@class='Dropdown - placeholder is -selected']")
    # Поле ввода Цвет самоката
    SCOOTER_COLOR = (By.XPATH, "//input[@type='checkbox' and text{}]")
    # Поле ввода Комментарий
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Кнопка Заказать
    BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    # Кнопка в окне Хотите оформить заказ "Да№
    PLACE_AN_ORDER = (By.XPATH, "//button[text()='Да']")
    # Кнопка в окне Заказ оформлен "Посмотреть статус"
    VIEW_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")




