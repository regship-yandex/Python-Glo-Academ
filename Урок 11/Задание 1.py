n = int(input())
number = []
for i in range(n):
    number.append(input())
print(*number)
srch = input('Слово для поиска: ')
i=0
while i < len(number):
    if number[i].lower().find(srch.lower())!= -1:
        print(number[i])
    i += 1