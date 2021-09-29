n = int(input())
minimum = n
maximum = 0
for i in range(n):
    number = int(input())
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number
print('Минимум равен', minimum)
print('Максимум равен', maximum)
