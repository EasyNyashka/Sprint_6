import allure
import pytest
import data
from pages.question_answer import QuestionAnswer


@allure.feature("Проверка раздела 'Вопросы о важном'")
class TestQuestionAnswer:
    @allure.title("Проверка ответа на вопрос №{index}")
    @pytest.mark.parametrize("index, expected_answer", data.Data.ACCORDION_DATA)
    def test_faq_answers(self, driver, index, expected_answer):
        question_answer = QuestionAnswer(driver)
        question_answer.click_question(index)
        answer_text = question_answer.get_answer_text(index)
        assert answer_text == expected_answer