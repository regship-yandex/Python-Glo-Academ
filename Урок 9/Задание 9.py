n = int(input())
n1 = n
counter = 10
while counter >= 10:
    counter = 0
    while n1 != 0:
        last_digit = n1 % 10
        n1 = n1 // 10
        counter += last_digit
    n1 = counter
print(counter)