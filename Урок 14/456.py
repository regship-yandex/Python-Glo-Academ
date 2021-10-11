
import random
# Проверяет правильный цифровой символ для длины пароля






def main_func():
    # Приветствие
    print('Привет. Я програма созодания пароля.')
    lenght_pass = 10
    num_pass = 2
    symbol_kit = ''
    while True:
        m = menu() # получаем значение переменной m из функции menu
        if m == 1:# длина пароля
            length_pass = (input())
            correct_num(length_pass)
        elif m == 2:    # Вывести "Введите длину пароля"
            # Количество паролей num_pass = 2
            print('Сейчас можно получить', num_pass)

        elif m == 3:
            symbol_kit = set_chart() # Набор символов
            print('что либо33')
        elif m == 4:
            # Генерация пароля
            print('что либо44')
        elif m == 0:  # Заканчиваем программу
            print('Программа закончена, до свидания')
            break
        else:
            print('что либо 1 ')
    else:
        print('что либо 2')


def is_valid(length_input):
    if length_input.isdigit():
         number = int(length_input)
         if 1 <= number:
             return True
    return False
def menu ():
    print('Текущие настройки такие:')
    print('Все настройки45646')
    print('1 - ')
    print('2 - ')
    print('3 - ')
    print('4 - ')
    print('0 - ')
    m = int(input())
    if False:
        m = -1
    return m

def int_input (str, defvalue):# ?????
    print(str)
    m = int(input())
    if is_valid(m):
        m = defvalue
    return m
def correct_num(length_input):# Проверка на корректный ввод длинны пароля
    if length_input.isdigit():
        num = int(input(length_input))
        if 1 <= num:
            return True
    return False

def char_selt(ask_symb):
    ask_symb = input()
    if ask_symb in 'lf Lf LF ДА Да да':
        Yes =  True
    else:
        Yes = False
# формируем набор символов, передаем
def set_chart():

    # Задаем вопросы и выбираем типы символов

    # enabled characters
    Yes = char_selt(input())
    enabled_chars = ''
    digits = '0123456789'
    # latin_lowercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # latin_uppercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    # russian_lowercase_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    # russian_uppercase_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    # punctuation = '!#%&*=-+_@ˆ'

    if digits_enabled == Yes:
        enabled_chars += digits
    else:
        enabled_chars += ''
    # if latin_lowercase_enabled == Yes:
    #     enabled_chars += latin_lowercase_letters
    #
    # if latin_uppercase_enabled == Yes:
    #     enabled_chars += latin_uppercase_letters
    #
    # if russian_lowercase_enabled == Yes:
    #     enabled_chars += russian_lowercase_letters
    #
    # if russian_uppercase_enabled == Yes:
    #     enabled_chars += russian_uppercase_letters
    #
    # if punctuation_enabled == Yes:
    #     enabled_chars += punctuation
    print(enabled_chars, 111233)
    return enabled_chars


# на входе длинна пароля и набор символов
def gen_pass():
    return

main_func()



# Спрашиваем какие сиволы включать в пароль

# Проверяем выбран ли хоть какой-то тип символов

# Формируем строку из возможных символов на основе ответов пользователя

# Генерируем пароль нужной длины из выбранных групп символов
