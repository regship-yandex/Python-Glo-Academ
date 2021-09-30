a = int(input())
whole = a
total = 0
b = whole % 2
while b == 0:
    whole = whole // 2
    b = whole % 2
    total += 1
    print('Сумма: ', total)
print(total)