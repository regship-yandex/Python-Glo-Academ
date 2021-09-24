data = int(input('Введите четырехзначное число: '))

hour = data //3600
minute = (data - hour*3600)//60
second = data - hour*3600 - minute*60

print(hour, 'час', minute, 'мин', second, 'сек')
