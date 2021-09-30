a = int(input())
total = a
sum_digit = 0
while a != 0:
    last_digit = a % 10
    sum_digit += last_digit
    a = a // 10
    # print(total, sum_digit)
total = total % sum_digit
if total == 0:
    question = 'YES'
elif total !=0:
    question = 'NO'
print(question)