
def get_next_leap_year(year):
    # Find the next year that is divisible by 4
    next_year = year + 1
    while next_year % 4 != 0:
        next_year += 1
    
    # Check if the next year is also divisible by 100
    if next_year % 100 == 0:
        # If the next year is divisible by 100, check if it is also divisible by 400
        if next_year % 400 == 0:
            return next_year
        else:
            return next_year + 1
    else:
        return next_year

def get_next_same_calendar_year(year):
    # Find the next leap year
    next_leap_year = get_next_leap_year(year)
    
    # Check if the next leap year has the same number of days as the current year
    if next_leap_year % 4 == 0:
        return next_leap_year
    else:
        return next_leap_year + 1

if __name__ == '__main__':
    year = int(input())
    print(get_next_same_calendar_year(year))

