e_mail = input('Введите адрес элфектронной почты: ')

if '@' in e_mail and '.' in e_mail:
    print('Корректный')
else:
    print('Некорректный')