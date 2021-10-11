def update_user_word(secret_word, user_word, char):
    new_user_word = ''
    for i in range(len(secret_word)):
        if secret_word[i] == char:
            new_user_word += char
        else:
            new_user_word += user_word[i]

    return new_user_word
def valid_char(char):
    if char in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        return char
    else:
        print('внимательно вводите букву')
        return ''
def word_stars(star):
    word = ''
    n = len(star)
    for i in range(n):
        word += '*'
    return word


while True:
    secret_word = 'ПарАвоз'
    secret_word =secret_word.lower()
    user_word = word_stars(secret_word)
    print(user_word, secret_word)
    while user_word != secret_word:
        print('Введите букву')
        user_char = valid_char(input())
        user_char = user_char.lower()
        if len(user_char) != 1:
            continue

        new_user_word = update_user_word(secret_word, user_word, user_char)

        if user_word == new_user_word:
            print('К сожалению, такой буквы нет в слове')
        else:
            print('Поздравляем, такая буква есть в слове')

        user_word = new_user_word
        print(user_word)

    print('Ура, вы угадали загаданное слово')

    output = input('Хотите еще сыграть? (да, нет)')
    if output in 'lfLfLFДаДАда':
       True
    else:
       print('Мы прощаемся с вами')
       False
