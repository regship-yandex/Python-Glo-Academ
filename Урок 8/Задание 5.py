a = int(input())
negative = 0
positive = 0
while a != 0:
    if a > 0:
        positive += 1
    if a < 0:
        negative += 1
    a = int(input())
print(positive*negative)
