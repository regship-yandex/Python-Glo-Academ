import random


def is_valid(int_input):
    if int_input.isdigit():
        t = int(int_input)
        if 1 <= t:
            return True
    return False


def int_input(str, defvalue):  # str =сторка вопрос / defvalue =  значение если ведино не верно
    print(str)
    m = input()
    if is_valid(m):
        m = int(m)
    else:
        m = defvalue
    return m


def get_length_pass(n):  # Длина пароля
    ret = int_input("Введите длину пароля", n)
    return ret


def get_num_pass(n):  # Количество паролей
    ret = int_input("Введите количество паролей", n)
    return ret


def gen_pass(length_pass, num_pass, symbol_kit):

    for t in range(num_pass):
        password = ''

        for j in range(length_pass):
            random_index = random.randint(0, len(symbol_kit) - 1)
            password += symbol_kit[random_index]
        print('Ваш пароль:', password)
    return


def ask_question(question):
    print(question, 'Нажмите Да или Нет')
    answer = input()
    if answer in 'ДаlfLfLFДАда':
        return 'Да'
    else:
        return 'Нет'


def get_symbol_kit(symbol_kit):
    # Спрашиваем какие сиволы включать в пароль
    enabled_chars = ''
    digits = '0123456789'
    latin_lowercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    latin_uppercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    russian_uppercase_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    russian_lowercase_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    punctuation = '!#%&*=-+?_@ˆ'

    digits_enabled = ask_question('Влючить цифры?')
    latin_lowercase_enabled = ask_question('Влючить строчные латинские буквы?')
    latin_uppercase_enabled = ask_question('Влючить прописные латинские буквы?')
    russian_lowercase_enabled = ask_question('Влючить строчные русские буквы?')
    russian_uppercase_enabled = ask_question('Влючить прописные русские буквы?')
    punctuation_enabled = ask_question('Влючить знаки пунктуации?')

    if digits_enabled == 'Да':
        enabled_chars += digits
    if latin_lowercase_enabled == 'Да':
        enabled_chars += latin_lowercase_letters
    if latin_uppercase_enabled == 'Да':
        enabled_chars += latin_uppercase_letters
    if russian_lowercase_enabled == 'Да':
        enabled_chars += russian_lowercase_letters
    if russian_uppercase_enabled == 'Да':
        enabled_chars += russian_uppercase_letters
    if punctuation_enabled == 'Да':
        enabled_chars += punctuation
    if enabled_chars == '':
        print('Вы не вабрали ни одной группы симваолов.\nПотому пароль будет состоять из прописных английских символов')
        return latin_uppercase_letters
    return enabled_chars


def menu():
    print('Меню введите:')
    print('1 - Чтобы изменить длину пароля')
    print('2 - Чтобы изменить количество паролей')
    print('3 - Чтобы изменить набор символов')
    print('4 - Генерация пароля')
    print('0 - Выход ')
    m = input()
    if m.isdigit():
        m = int(m)
    return m


def main_func():
    # Приветствие
    print('\nПривет. Я програма созодания пароля.\n')
    length_pass = 8
    num_pass = 1
    symbol_kit = 'symbol_kit'
    while True:
        print('Текущие настройки такие:')
        print("Длина пароля =", length_pass, "Количество генерируемыых паролей =", num_pass)
        m = menu()  # получаем значение переменной m из функции menu
        if m == 1:  # длина пароля
            length_pass = get_length_pass(length_pass)
        # correct_num(length_pass)
        elif m == 2:  # количество паролей
            print('Сейчас можно получить', num_pass)
            num_pass = get_num_pass(num_pass)
        elif m == 3:  # набор символов
            symbol_kit = get_symbol_kit(symbol_kit)  # Набор символов
        elif m == 4:  # Генерация пароля
            gen_pass(length_pass, num_pass, symbol_kit)

        elif m == 0:  # Заканчиваем программу
            print('Программа закончена, до свидания')
            break
        else:
            print('что не то ввели ', m)
    else:
        print('пока')


main_func()
