n = int(input('Число:'))
if n == 1:
    total = 0
else:
    total = 1

for i in range(n+1):
        if i % 10 == 2 or i % 10 == 9:
            total = total * i
print(total)