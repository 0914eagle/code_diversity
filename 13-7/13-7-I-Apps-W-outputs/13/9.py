
def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def get_next_leap_year(year):
    while True:
        year += 1
        if is_leap_year(year):
            return year

def get_calendar_year(year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29
    return days_in_month

def get_next_same_calendar(year):
    days_in_month = get_calendar_year(year)
    next_year = get_next_leap_year(year)
    next_days_in_month = get_calendar_year(next_year)
    while next_days_in_month != days_in_month:
        next_year = get_next_leap_year(next_year)
        next_days_in_month = get_calendar_year(next_year)
    return next_year

def main():
    year = int(input())
    print(get_next_same_calendar(year))

if __name__ == '__main__':
    main()

