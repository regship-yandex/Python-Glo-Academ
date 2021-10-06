digit1 = int(input('Число первое: '))
digit2 = int(input('Число второе: '))
def numeric (digital):
    total = 0
    while digital > 0:
        total += 1
        digital = digital // 10
    return total
numeric_dig1 = numeric(digit1)
numeric_dig2 = numeric(digit2)
print(numeric_dig1*numeric_dig2)