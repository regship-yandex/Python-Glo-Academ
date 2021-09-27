ticket = int(input('Введите номер билета: '))

left_data = ticket // 1000
right_data = ticket % 1000

left_data1 = left_data // 100
left_data2 = left_data % 100 //10
left_data3 = left_data % 10
left_summ = left_data1 + left_data2 +left_data3
left_summ = left_data1 + left_data2 +left_data3

right_data1 = right_data // 100
right_data2 = right_data % 100 //10
right_data3 = right_data % 10
right_summ = right_data1 + right_data2 +right_data3

if left_summ == right_summ:
    print('Билет', ticket, 'счастливый')

else:
    print('Билет', ticket, 'Несчастливый')
