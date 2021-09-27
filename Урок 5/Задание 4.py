w = int(input('Введите вес от 1 до 100 кг: '))
w1 = w % 2
if w >= 2 and w <= 100 and w1 == 0:
    part1 = int(input('Введите вес одной из частей: '))
    part1 = part1 % 2
    if part1 == 0:
        part2 = (w - part1) % 2
        if part2 == 0:
            print('YES')
    else:
        print('NO')
else:
    print('NO')