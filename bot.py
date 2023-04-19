from functions import *

hello_message = """Привет! Предлагаю поиграть в викторину на английском языку.
Отвечай на вопросы и зарабатывай очки. Количество вопросов ты определяешь самостоятельно."""
print(hello_message)
question_amount_range = range(1, 101)
for i in range(2):
    user_input = input("Введи число от 1 до 100: ")
    # проверка, что инпут - целое число в промежутке от 1 до 100 (ограничение API)
    if user_input.isdigit() and int(user_input) in question_amount_range:
        question_amount = int(user_input)
        break
    else:
        question_amount = None
        print("Упс, неверный формат ввода.")  # Добавить что попробуй еще раз

total_score = 0
response = make_api_call(question_amount)
if response:
    # вывод вопросов и подсчет числа правильных ответов
    for i, element in enumerate(response.json()):
        print(element["answer"])  # УБРАТЬ ПЕРЕД ОТПРАВКОЙ
        print("\nВопрос {}: {}".format(i+1, element["question"]))
        total_score += score_user_answer(element["answer"].lower())
    print("Спасибо за игру! Твой результат: {}".format(total_score))
else:
    print("База вопросов что-то барахлит, не удается к ней подключиться. Попробуй еще раз позже.")