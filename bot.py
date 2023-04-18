# что добавлено?

#!pip install requests
import requests

def make_api_call(user_input):
    if not user_input: return None
    try:
        response = requests.get("http://jservice.io/api/random", params={"count": user_input})
        response.raise_for_status()
        return response
    except:
        print("База вопросов что-то барахлит, не удается к ней подключиться. Попробуй еще раз позже.")
        return None

def score_user_answer(correct_answer, max_attempts=2):
    for i in range(max_attempts):
        user_answer = input("Твой ответ: ").lower()
        if user_answer == correct_answer:
            print("Верный ответ")
            return 1
        print("Пока неверно. Попробуй еще раз: {}".format(elem["question"]))
    return 0

print("Привет! Предлагаю поиграть в викторину на английском языку. Отвечай на вопросы и зарабатывай очки. Число вопросов ты определяешь самостоятельно.")
input_range = range(1, 101)
for i in range(2):
    user_input = input("Введи число от 1 до 100: ")
    if user_input.isdigit() and int(user_input) in input_range:
        user_input = int(user_input)
        break
    else:
        user_input = None
        print("Упс, неверный формат ввода.") ## Добавить что попробуй еще раз

total_score = 0
response = make_api_call(user_input)
if response:
    for i, elem in enumerate(response.json()):
        print(elem["answer"])  # УБРАТЬ ПЕРЕД ОТПРАВКОЙ
        print("Вопрос {}: {}".format(i+1, elem["question"]))
        total_score += score_user_answer(elem["answer"].lower())
    print("Твой результат: {}".format(total_score))