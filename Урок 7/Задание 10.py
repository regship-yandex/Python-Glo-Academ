n = int(input('Сколько раз: '))
flag = 0
for i in range(n):
    number = int(input())
    if number % 2 != 0:
        flag += 1
if flag == n:
    print('YES')
else:
    print('NO')