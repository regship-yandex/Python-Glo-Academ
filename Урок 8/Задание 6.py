a = int(input())
while a <= 0:
    a = int(input('Введите число больше 0: '))
total = 0
summa = 0
while a != 0:
    summa += a
    total += 1
    a = int(input())
print(summa/total)