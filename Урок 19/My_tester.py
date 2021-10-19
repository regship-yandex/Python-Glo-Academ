import random
import pathlib
from asyncore import write
from pathlib import Path

queastions = [
    'Сколько будет два плюс два умноженное на два?',
    'Бревно нужно распилить на 10 частей, сколько надо сделать распилов',
    'На руках 10 пальцев. Сколько пальцев на 5 руках?',
    'Укол делают каждые полчаса, сколько нужно минут для трех уколов?',
    'Пять свечей сгорело, две потухли. Сколько свечей осталось?',
    'Ешо один вумный вопрос. Кто ответ знает?',
    'Cто первый вопрос',
    '500'
]
answer = [6, 9, 25, 60, 2, 100, 101, 500]
diagnosis = {5: 'Гений', 4: 'Талант', 3: 'Нормальный',
             2: 'Дурак', 1: 'Кретин', 0: 'Идиот', 'max': 5}
diagnosis_tmp = []
answer_tmp = []


def int_input(str):
    digit = input()
    while not is_valid(digit):
        digit = input()
    else:
        digit = int(digit)
    return digit


def is_valid(int_input):
    if int_input.isdigit():
        n = int(int_input)
        return True
    print('Пожалуйста, введите число!')
    return False


def mix_answer(len):
    mix = list(range(len))
    i = 0
    if i in range(len - 1):
        ran_num = random.randint(i, len - 1)
        tmp_mix = mix[ran_num]
        mix[ran_num] = mix[i]
        mix[i] = tmp_mix
    return mix


def file_recording(test_result):

    file = open("my_test.csv", 'a')
    file.write(test_result)
    file.close()


def calc_diagnosis(count_right_answer, queastions_len, diagnosis):

    max = diagnosis['max']
    cp = count_right_answer / queastions_len
    if 4/max <= cp <= 5/max:
        count = 5
    elif 3/max <= cp <= 4/max:
        count = 4
    elif 2/max <= cp <= 3/max:
        count = 3
    elif 1/max <= cp <= 2/max:
        count = 2
    elif 0/max <= cp <= 1/max:
        count = 1
    else:
        count = max
    return diagnosis[count]


def tester_function():
    count_right_answer = 0
    name = input('Представтесь, пожалуйста:')
    num_mix = mix_answer(len(queastions))
    for i in range(len(queastions)):
        num_random = num_mix[i]
        print(f'Вопрос № {i + 1}: {queastions[num_random]}')
        user_answer = int_input('')
        right_answer = answer[num_random]
        if user_answer == right_answer:
            count_right_answer += 1
    # print(f'Всего вопосов:{len(queastions)}')
    print(
        f'{name:8},вы дали правильных ответов {count_right_answer:5}, вас компьютер оценил как: {calc_diagnosis(count_right_answer, len(queastions) , diagnosis):5}')
    result_test = (
        f'{name:12}; {count_right_answer:9}; {calc_diagnosis(count_right_answer, len(queastions), diagnosis):8}\n')
    file_recording(result_test)


# Остновной код  #
while True:
    tester_function()
    output = input('Хотите повторить? (да, нет)')
    if not output in 'lfLfLFДаДАда':
        print('Мы прощаемся с вами')
        break
