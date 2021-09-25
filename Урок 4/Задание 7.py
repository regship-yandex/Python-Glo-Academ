num = int(input('Введите число от 100 до 1000000000: '))

num3 = num % 1000 // 100
num2 = num % 100 // 10
num1 = num % 10 
summ = num3 + num2 + num1

print('У числа', num, 'сумма последних трех цифр равна', summ)
