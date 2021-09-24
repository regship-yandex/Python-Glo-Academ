num = int(input('Вводим треххначное число число:'))

first = num // 100
second = num % 100//10
third = num % 10
result1 = first + second + third
result2 = first * second * third

print('Сумма цифр числа', num, 'равна', result1)             
print('Произведение цифр числа', num, 'равно', result2)
