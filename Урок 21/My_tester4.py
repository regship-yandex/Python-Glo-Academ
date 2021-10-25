# -*- coding: utf8 -*-
import random
from QuestionsStorage import QuestionStorage
from QuestionsStorage import EditQuestionStorage
from User import User
from UsersResultStorage import UserResultStorage


diagnosis = {5: 'Гений', 4: 'Талант', 3: 'Нормальный',
             2: 'Дурак', 1: 'Кретин', 0: 'Идиот', 'max': 5}


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




def calc_diagnosis(count_answer, queastions_len,
                   diagnosis):
    max = diagnosis['max']
    cp = count_answer / queastions_len
    if 4 / max <= cp <= 5 / max:
        count = 5
    elif 3 / max <= cp <= 4 / max:
        count = 4
    elif 2 / max <= cp <= 3 / max:
        count = 3
    elif 1 / max <= cp <= 2 / max:
        count = 2
    elif 0 / max <= cp <= 1 / max:
        count = 1
    else:
        count = max
    return diagnosis[count]


def tester_function():
    store_quest = QuestionStorage()
    # count_right_answer = 0
    queastions = store_quest.get_queastions()
    num_mix = mix_answer(len(queastions))
    user_name = input('Представтесь, пожалуйста:')
    user = User(user_name)
    user.count_right_answer = 0
    for i in range(len(queastions)):
        num_random = num_mix[i]
        print(
            f'Вопрос № {i + 1}: {queastions[num_random].text}')
        user_answer = int_input('')
        right_answer = queastions[num_random].answer
        if user_answer == right_answer:
            user.count_correct_answer()

    user.result = calc_diagnosis(
        user.count_right_answer, len(queastions), diagnosis)

    print(
        f'{user.name:8},вы дали правильных ответов '
        f'{user.count_right_answer:5}, вас компьютер оценил как: '
        f'{user.result:5}')
    urs = UserResultStorage()
    urs.add_user(user)


# Остновной код  #
while True:
    tester_function()
    output = input(
        'Хотите посмотреть резульататы? (да, нет)')
    if output in 'lfLfLFДаДАда':
        urs = UserResultStorage()
        urs.show_user_result()


    output = input(
        'Хотите изменить список вопросов ? (да, нет)')
    if output in 'lfLfLFДаДАда':
        eqs = EditQuestionStorage()
        eqs.menu()

    output = input('Хотите повторить? (да, нет)')
    if not output in 'lfLfLFДаДАда':
        print('Мы прощаемся с вами')
        break
