import requests
from fuzzywuzzy import fuzz

class Bot:
    def __init__(self):
        self.question_amount_range = range(1, 101)
        self.total_score = 0
        self.url = "http://jservice.io/api/random"

    def run(self):
        user_input = input("Введи число от 1 до 100: ")
        if user_input.isdigit() and int(user_input) in self.question_amount_range:
            question_amount = int(user_input)
        else:
            print("Упс, неверный формат ввода. Попробуй еще раз.")
            self.run()
            return
        response = self.make_api_call(question_amount)
        if response:
            for i, element in enumerate(response.json()):
                print("\nВопрос {}: {}".format(i+1, element["question"]))
                self.total_score += self.score_user_answer(element["answer"].lower())
            print("Спасибо за игру! Количество правильных ответов: {}".format(self.total_score))
        else:
            print("База вопросов что-то барахлит, не удается к ней подключиться. Попробуй еще раз позже.")

    def make_api_call(self, question_amount):
        if not question_amount:
            return None
        try:
            response = requests.get(self.url, params={"count": question_amount})
            response.raise_for_status()
            return response
        except:
            return None

    def is_answer_similar(self, user_answer, correct_answer, threshold=80):
        similarity_score = fuzz.token_set_ratio(user_answer, correct_answer)
        return similarity_score >= threshold
    
    def score_user_answer(self, correct_answer, max_attempts=2):
        for i in range(max_attempts):
            user_answer = input("Твой ответ: ").lower()
            if self.is_answer_similar(user_answer, correct_answer):
                print("Молодец! Твой ответ верный.\n")
                return 1
            print("Жаль, но твой ответ неправильный.\n") if i == 1 else print("Пока неверно. Попробуй еще раз.")
        return 0
    
if __name__ == "__main__":
    print("Привет! Предлагаю поиграть в викторину на английском языку. Отвечай на вопросы и зарабатывай очки. Количество вопросов ты определяешь самостоятельно.")
    bot = Bot()
    bot.run()