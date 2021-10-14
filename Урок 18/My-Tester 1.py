import random

queastions = [
    'Сколько будет два плюс два умноженное на два?',
    'Бревно нужно распилить на 10 частей, сколько надо сделать распилов',
    'На руках 10 пальцев. Сколько пальцев на 5 руках?',
    'Укол делают каждые полчаса, сколько нужно минут для трех уколов?',
    'Пять свечей сгорело, две потухли. Сколько свечей осталось?'
]
answer = [6, 9, 25, 60, 2]
diagnosis = {5: 'Гений', 4: 'Талант', 3: 'Нормальный',
             2: 'Дурак', 1: 'Кретин', 0: 'Идиот'}
diagnosis_tmp = []
answer_tmp = []


def int_input(str):
    print(str)
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
    return False


# def random_queast(count_queast):
# n = 0
# while n < count_queast:
#     t = random.randint(0, count_queast)
#     print('Номер вопроса:', t)
#     return t

def mix_answer(len):
    mix = list(range(len))
    i = 0
    if i in range(len - 1):
        ran_num = random.randint(i, len - 1)
        tmp_mix = mix[ran_num]
        mix[ran_num] = mix[i]
        mix[i] = tmp_mix
    return mix


# Остновной код  #
while True:
    count_right_answer = 0
    name = input('Представтесь, пожалуйста:')
    num_mix = mix_answer(len(queastions))
    for i in range(len(queastions)):
        num_random = num_mix[i]
        print('Вопрос:', i + 1, queastions[num_random])
        user_answer = int_input('')
        right_answer = answer[num_random]
        if user_answer == right_answer:
            count_right_answer += 1

    print(name, 'вы дали правильных ответов', count_right_answer, '\nвас компьютер оценил как:', diagnosis[count_right_answer])

    output = input('Хотите повторить? (да, нет)')
    if output in 'lfLfLFДаДАда':
        continue
    else:
        print('Мы прощаемся с вами')
        break
