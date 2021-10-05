strng = [1, 3, 2, 4, 2]
countg = []
for i in range(len(strng)):
    symbol = strng.count(strng[i])
    if symbol == 1:
        a = countg.append(strng[i])
print(*countg)