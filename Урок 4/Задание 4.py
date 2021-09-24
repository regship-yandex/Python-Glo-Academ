r= int(input())
k= int(input())
n= int(input())

price = r + k/100
sum = price * n

rub = int(sum // 1)
kop = int(sum * 100 % 100)
print('За', n, 'мяч. нужно заплатить', rub, 'руб.', kop, 'коп.')
