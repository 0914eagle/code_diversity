
def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def get_days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 30

def get_days_in_year(year):
    days = 0
    for month in range(1, 13):
        days += get_days_in_month(month, year)
    return days

def get_same_calendar_year(year):
    next_year = year + 1
    while True:
        if get_days_in_year(next_year) == 366:
            return next_year
        next_year += 1

def main():
    year = int(input())
    print(get_same_calendar_year(year))

if __name__ == '__main__':
    main()

