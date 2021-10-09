# Загадать число от 1 до 100
# Организовать опрос поля
# Ввести число
# Если загаданное число больше чем введенное число-больше
# Если загаданное число меньше чем введенное число-меньше
# Если загаданное число равно введенному числу - Победа!
# До новых встреч
import math
from random import *    # библиотека одна
def is_valid(user_input, max):
    if user_input.isdigit():
        user_number = int(user_input)
        if  1 <= user_number  and user_number <= max:
            return True

    return False

def sold_out ():
    secret_number = 0
    max = 100
    while True:
        #print('Хотите продолжить? Введите [y]или[n]')
        print('Начать Игру? Введите [y]или[n]')
        answer = input()
        if not (answer == 'y' or answer == 'н'):
            break

        max = int(input("max правую границу "))
        secret_number = randint(1, max)
        # print('я загодал число от 1 до ', max ,"по секрету " , secret_number)
        print('я загодал число от 1 до', max)
        main_function(secret_number, max)
    print('Пока пока...')


def main_function(secret_number, max):
    total=0

    while True:
        print('Введите число от 1 до', max)
        user_number = input()
        if not is_valid(user_number, max):
            continue
        user_number = int(user_number)
        total += 1
        if secret_number > user_number:
            print('Загаданное число больше, чем введенное вами число')
        elif secret_number < user_number:
            print('Загаданное число меньше, чем введенное вами число')
        else:
            print('Ура! Вы угудали число за', total, 'ходов!\nОптимальное число ходов равно:')
            print(int(math.log2(max)), 'ходов')
            print('Раунд окончен')
            break


#secrert_number = randint(1, 100)
print('Добро пожаловать в игру "Угадай число"')
sold_out ()
#main_function(secrert_number, total)