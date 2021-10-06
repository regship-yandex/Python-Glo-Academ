list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

def max_digit(list):
    list_max = max(list)
    return list_max
list_max1 = max_digit(list1)
list_max2 = max_digit(list2)
print(list_max1*list_max2)
