number = '1 3 2 4 2'
count = []
i = 0
num_sp = number.split(" ")
print('num_sp: ', num_sp)
while i < len(num_sp):
    j = i + 1
    litera = num_sp[i]
    print(i, litera)
    while j < len(num_sp):
        print(i, j)
        print(litera, number.count(j))
        if litera != number.count(j):
            print(count, '+ + ')
        j += 1
    i += 1
print(count)