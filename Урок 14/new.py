import random
# Блок с функциями

def zadat_vopros(question):  # ask_question
    print(question, 'Нажмите Да или Нет')
    answer = input()
    if answer in 'ДаlfLfLFДАда':
        return 'Да'
    else:
        return 'Нет'


def is_valid(length_input):
     while True:  # ввод символа переносим в это место
        length_input = input()
        if length_input.isdigit():
            number = int(length_input)
            if 1 <= number:
                return number

#               Основной блок кода                 #

# Приветствие
print('Привет. Я генератор паролей')
# Вывести "Введите длину пароля"
length = 0
length = is_valid(length)  # Получаем длину пароля
# print(length, 11)
# Спрашиваем какие сиволы включать в пароль
enabled_chars = ''
digits = '0123456789'
# latin_lowercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
latin_uppercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# russian_lowercase_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# russian_uppercase_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# punctuation = '!#%&*=-+?_@ˆ'

digits_enabled = zadat_vopros('Влючить цифры?')
# latin_lowercase_enabled = ask_question('Влючить строчные латинские буквы?')
latin_uppercase_enabled = zadat_vopros('Влючить прописные латинские буквы?')
# russian_lowercase_enabled = ask_question('Влючить строчные русские буквы?')
# russian_uppercase_enabled = ask_question('Влючить прописные русские буквы?')
# punctuation_enabled = ask_question('Влючить знаки пунктуации?')
# Проверяем выбран ли хоть какой-то тип символов
# Формируем строку из возможных символов на основе ответов пользователя


if digits_enabled == 'Да':
    enabled_chars += digits
    print(1, enabled_chars)
# if latin_lowercase_enabled == 'Да':
#     enabled_chars += latin_lowercase_letters
#     print(2)
if latin_uppercase_enabled == 'Да':
    enabled_chars += latin_uppercase_letters
    print(3,enabled_chars)
# if russian_lowercase_enabled == 'Да':
#     enabled_chars += russian_lowercase_letters
#     print(4)
# if russian_uppercase_enabled == 'Да':
#     enabled_chars += russian_uppercase_letters
#     print(5)
# if punctuation_enabled == 'Да':
#     enabled_chars += punctuation
#     print(6)
print('Набор символов:', enabled_chars, latin_uppercase_enabled)

# Генерируем пароль нужной длины из выбранных групп символов
password = ''
total = 0

for i in range(int(length)):
    random_index = random.randint(0, len(enabled_chars) - 1)
    password += enabled_chars[random_index]
    total += 1
print(password)
