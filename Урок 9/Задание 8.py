a = int(input())
counter = 0
while a != 0:
    last_digit = a % 10
    a = a // 10
    if last_digit == 5:
        counter += 1
print(counter)