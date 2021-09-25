data = int(input('Вводим 4х значное число: '))

a = data //1000
b = data // 100 % 10
c = data // 10 % 10
d = data % 10

e = max(a, b, c, d)

print ('Учила', data, 'максимальная цифра равна', e)
