import unittest
import requests
from unittest.mock import patch
from functions import *

class TestMakeApiCall(unittest.TestCase):
    # успешный вызов API
    def test_make_api_call_valid_input(self):
        with patch("requests.get") as mock_get:
            mock_response = requests.Response()
            mock_response.status_code = 200
            mock_get.return_value = mock_response

            result = make_api_call(2)

            mock_get.assert_called_once_with(
                default_url,
                params={'count': 2}
            )
            self.assertEqual(result, mock_response)

    # число вопросов для викторины не определено
    def test_make_api_call_invalid_input(self):
        result = make_api_call(None)
        self.assertIsNone(result)

    # неуспешный вызов API
    def test_make_api_call_error_response(self):
        with patch("requests.get") as mock_get:
            mock_response = requests.Response()
            mock_response.status_code = 404
            mock_get.return_value = mock_response

            result = make_api_call(3)

            mock_get.assert_called_once_with(
                default_url,
                params={'count': 3}
            )
            self.assertIsNone(result)

class TestsScoreUserAnswer(unittest.TestCase):
    # верный ответ
    def test_score_user_answer_right(self):
        with patch('builtins.input', return_value="USA"):
            assert score_user_answer("the USA") == 1

    # 2 неверных ответ
    def test_score_user_answer_wrong(self):
        with patch('builtins.input', side_effect=["Canada", "Mexico"]):
            assert score_user_answer("the USA") == 0

    # верная вторая попытка
    def test_score_user_answer_second_attempt(self):
        with patch('builtins.input', side_effect=["Canada", "USA"]):
            assert score_user_answer("apple") == 0

if __name__ == "__main__":
    unittest.main()