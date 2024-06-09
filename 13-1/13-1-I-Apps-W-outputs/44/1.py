
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def days_between_dates(date1, date2):
    years_diff = int(date2[:4]) - int(date1[:4])
    months_diff = int(date2[5:7]) - int(date1[5:7])
    days_diff = int(date2[8:]) - int(date1[8:])

    days = 0
    for i in range(years_diff):
        if is_leap_year(int(date1[:4]) + i):
            days += 366
        else:
            days += 365
    days += days_diff

    for i in range(months_diff):
        if is_leap_year(int(date1[:4])):
            days += [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][i]
        else:
            days += [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][i]

    return days

