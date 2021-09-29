num = int(input('Сколько чисел ввести?: '))

nummin, nummax = num, num
for i in range(num):
    number = int(input())
    if number > nummax:
        nummax = number
    elif number < nummin:
        nummin = number
print('Максимум равен: ', nummax)
print('Минимум равен: ', nummin)
