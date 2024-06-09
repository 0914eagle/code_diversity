
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def days_between_dates(date1, date2):
    years_diff = int(date2[:4]) - int(date1[:4])
    months_diff = int(date2[5:7]) - int(date1[5:7])
    days_diff = int(date2[8:]) - int(date1[8:])

    days = 0
    for year in range(int(date1[:4]), int(date2[:4]) + 1):
        days += 365
        if is_leap_year(year):
            days += 1
    for month in range(1, months_diff + 1):
        days += 31
        if month in [4, 6, 9, 11]:
            days -= 1
        elif month == 2:
            if is_leap_year(year):
                days += 29
            else:
                days += 28
    days += days_diff

    return days

