a = int(input())
flag = 0
n = a
for i in range(a, 0, -1):
    t = a % i
    if t == 0:
        flag += 1
if flag < 3:
    print('YES')
else:
    print('NO')

