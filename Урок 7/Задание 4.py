a = int(input('Число a: '))
b = int(input('Число b: '))
if a > b:
    a, b = b, a
for i in range(a, b+1):
    counter = i
    if counter % 2 == 0:
        print(counter)