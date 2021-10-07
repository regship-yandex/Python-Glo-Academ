from random import *
min_num = 1
max_num = 100

num_secret = randint(1, 100)
magic_number = 50
print(num_secret)
# Проверка  чисел
total = 0
while True:

    if magic_number < num_secret:
        min_num = magic_number
        tmp = max_num - min_num
        magic_number = tmp // 2 + min_num
        total += 1
    elif magic_number > num_secret:
        max_num = magic_number
        tmp = (max_num - min_num)
        magic_number = max_num - tmp // 2
        total += 1
    else:
        print('Угадал за', total, 'ходов', num_secret, '=', magic_number)
        break
