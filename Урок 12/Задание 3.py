month = int(input())
def month_day(month):
    month = month - 1
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mon = day[month]
    return mon
print(month_day(month))