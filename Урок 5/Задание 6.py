pt = int(input('Ent r Da :'))
ev_odd = pt % 2
if pt <0 or pt > 36:
    print(pt, 'Вне диапазона')
elif pt == 0:
    print(pt, 'Зелёный')
elif (pt>0 and pt<=10) or (pt>=19 and pt<=28):
    if ev_odd == 0:
        print(pt, 'Чётный-чёрный')
    else:
        if ev_odd != 0:
            print(pt, 'Нечётный-красный')
elif (pt>=11 and pt<=18) or (pt>=29 and pt<=36):
    if ev_odd == 0:
        print(pt, 'Чётный-красный')
    else:
        if ev_odd != 0:
            print(pt, 'Нечётный-чёрный')
