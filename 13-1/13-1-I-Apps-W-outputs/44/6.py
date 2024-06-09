
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def days_between_dates(date1, date2):
    years_diff = int(date2[:4]) - int(date1[:4])
    months_diff = int(date2[5:7]) - int(date1[5:7])
    days_diff = int(date2[8:]) - int(date1[8:])

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_months[1] = 29 if is_leap_year(int(date1[:4])) else 28

    total_days = days_diff
    for i in range(months_diff):
        total_days += days_in_months[i]

    for i in range(years_diff):
        total_days += 365
        if is_leap_year(int(date1[:4]) + i):
            total_days += 1

    return total_days

