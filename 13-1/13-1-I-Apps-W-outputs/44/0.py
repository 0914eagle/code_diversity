
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 30

def days_between_dates(date1, date2):
    years_diff = int(date2[:4]) - int(date1[:4])
    months_diff = int(date2[5:7]) - int(date1[5:7])
    days_diff = int(date2[8:]) - int(date1[8:])

    days = 0
    current_date = date1
    for i in range(years_diff):
        days += 365
        if is_leap_year(int(current_date[:4]) + i):
            days += 1

    for i in range(months_diff):
        days += days_in_month(int(current_date[:4]), int(current_date[5:7]) + i)

    days += days_diff

    return days

date1 = input()
date2 = input()
print(days_between_dates(date1, date2))

