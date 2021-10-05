number = '1 2 1 1 4'
count = 0
i = 0
num_sp = number.split(" ")
while i < len(num_sp):
    j = i + 1
    litera = num_sp[i]
    while j < len(num_sp):
        num_data = num_sp[j]
        if litera == num_data:
            count += 1
        j += 1
    i += 1
print(count)