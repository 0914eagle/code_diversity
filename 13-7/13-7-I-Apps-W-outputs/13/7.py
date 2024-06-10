
def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def find_next_leap_year(year):
    while True:
        year += 1
        if is_leap_year(year):
            return year

def find_next_calendar_year(year):
    while True:
        year += 1
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return year

def main():
    year = int(input())
    next_leap_year = find_next_leap_year(year)
    next_calendar_year = find_next_calendar_year(year)
    print(next_calendar_year)

if __name__ == '__main__':
    main()

