import sys
import json


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    count = 0
    for item in data['game']['rounds']:
        if item['questions']:
            count += 1
    print(count)


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    correct_answer = []
    for item in data['game']['rounds']:
        for i in item['questions']:
            correct_answer.append(i['correct_answer'])
    print(correct_answer)


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    full_time_to_answer = []
    for item in data['game']['rounds']:
        full_time_to_answer.append(item['settings']['time_to_answer'])
        for i in item['questions']:
            try:
                full_time_to_answer.append(i['time_to_answer'])
            except:
                pass
    max_time_to_answer = max(full_time_to_answer)
    print(max_time_to_answer)


def main(filename):
    with open(filename) as f:
        data = json.load(f)  # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    filename = sys.argv[2]  # передается с помощью запуска через cmd команды (py 4.py -v "test.json")
    print(filename)
    main(filename)
