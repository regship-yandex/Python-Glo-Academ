ticket = int(input('Введите номер билета: '))

ld = ticket // 1000
rd = ticket % 1000

ld1 = ld // 100
ld2 = ld % 100 //10
ld3 = ld % 10
ls = ld1 + ld2 +ld3
ls = ld1 + ld2 +ld3

rd1 = rd // 100
rd2 = rd % 100 //10
rd3 = rd % 10
rs = rd1 + rd2 +rd3

if ls == rs:
    print('Билет', ticket, 'счастливый')

else:
    print('Билет', ticket, 'Несчастливый')
