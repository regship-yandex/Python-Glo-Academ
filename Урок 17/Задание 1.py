import random


def generate_secret_word():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    secret_word = ''
    for i in range(4):
        random_index = random.randint(0, len(digits) - 1)
        secret_word += str(digits[random_index])
        digits.pop(random_index)
    return secret_word


def calculate_bulls_count(user_word, secret_word):
    counter = 0
    for i in range(len(secret_word)):
        if secret_word[i] == user_word[i]:
            counter += 1
    return counter


def calculate_cows_count(user_word, secret_word):
    counter = 0
    for i in range(len(user_word)):
        if secret_word[i] != user_word[i] and user_word[i] in secret_word:
            counter += 1
    return counter


def valid_input(len_secret):
    while True:
        symb = ''
        user_word = input()
        if not user_word.isdigit():
            continue
        len_user_word = len(user_word)
        len_secret_word = len(secret_word)
        if len_user_word != len_secret_word:
            continue
        if not recurring_chars(user_word):
            continue

        return user_word


def recurring_chars(user_word):
    len_word = len(user_word)
    symb = ''
    for i in range(len_word):
        symb = user_word[i]
        if user_word.count(symb) > 1:
            return False
        else:
            return True




# Основной код  #

while True:  # Повтор игры
    secret_word = generate_secret_word()
    print(secret_word)
    print("Найди число")
    while True:  # Начало игры
        user_word = valid_input(secret_word)  # input('Введи свое число:')
        bulls_count = calculate_bulls_count(user_word, secret_word)
        cows_count = calculate_cows_count(user_word, secret_word)

        print(bulls_count, 'быков', cows_count, 'коров')

        if bulls_count == len(secret_word):
            print(bulls_count, 'Ура! Ты победил!')
            break

    output = input('Хотите еще сыграть? (да, нет)')
    if output in 'lfLfLFДаДАда':
        continue
    else:
        print('Мы прощаемся с вами')
        break
