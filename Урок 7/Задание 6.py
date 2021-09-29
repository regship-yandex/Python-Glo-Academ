counter = int(input('Число:'))
total = 0

for i in range(counter+1):
    if i % 10 == 1 or i % 10 == 3 or i % 10 == 7:
        total = total + i
print(total)