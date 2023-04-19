#!pip install requests
#!pip install fuzzywuzzy
import requests
from fuzzywuzzy import fuzz

default_url = "http://jservice.io/api/random"

# функция выполняет API запрос и возвращает его, если он успешен
def make_api_call(question_amount, url=default_url):
    if not question_amount:
        return None
    try:
        response = requests.get(url, params={"count": question_amount})
        response.raise_for_status()
        return response
    except:
        return None

# функция определяет, достаточно ли похожи запросы
def is_answer_similar(user_answer, correct_answer, threshold=80):
    similarity_score = fuzz.token_set_ratio(user_answer, correct_answer)
    return similarity_score >= threshold

# функция получает ответ пользователя и оценивает его правильность
def score_user_answer(correct_answer, max_attempts=2):
    for i in range(max_attempts):
        user_answer = input("Твой ответ: ").lower()
        if is_answer_similar(user_answer, correct_answer):
            print("Молодец! Твой ответ верный.\n")
            return 1
        print("Жаль, но твой ответ неправильный.\n") if i == 1 else print("Пока неверно. Попробуй еще раз.")
    return 0