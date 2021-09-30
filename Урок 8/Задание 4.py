a = 32312146847
minimum = a % 10
maximum = a % 10
while a != 0:
    last = a % 10
    a = a // 10
    if last < minimum:
        minimum = last
    if last > maximum:
        maximum = last
print('Максимум равен', maximum)
print('Минимум равен', minimum)
