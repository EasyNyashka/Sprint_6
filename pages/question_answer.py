import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class QuestionAnswer(BasePage):

    @allure.step("Нажать на вопрос с индексом {index}")
    def click_question(self, index):
        locator = HomePageLocators.fag_questions_items[index]
        self.wait_for_element(HomePageLocators.COOKIE)
        self.click_on_element(HomePageLocators.COOKIE)
        self.scroll_to_element(locator)
        self.wait_for_element(locator)
        self.click_on_element(locator)

    @allure.step("Получить текст ответа для вопроса {index}")
    def get_answer_text(self, index):
        locator = HomePageLocators.faq_answers_items[index]
        return self.get_text_on_element(locator)

