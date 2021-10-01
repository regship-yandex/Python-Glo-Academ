number = int(input())
flag = 0

while number != 0:
    last = number % 10
    if last == 1:
        flag += 1
        break
    number = number // 10
if flag > 0:
    print('YES')
else:
    print('NO')