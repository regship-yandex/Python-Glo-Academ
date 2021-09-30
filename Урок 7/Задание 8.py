n = int(input())
number = int(input())
minimum = number
maximum = number
for i in range(n-1):
    number = int(input())
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number
print('Минимум равен', minimum)
print('Максимум равен', maximum)
