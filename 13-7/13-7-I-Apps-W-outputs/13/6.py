
def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def next_same_calendar_year(year):
    while True:
        year += 1
        if is_leap_year(year):
            if year % 4 == 0 and (year - 1) % 100 != 0 or year % 400 == 0:
                return year
        else:
            if year % 4 == 0 and (year - 1) % 100 == 0 and (year - 1) % 400 != 0:
                return year

def main():
    year = int(input())
    print(next_same_calendar_year(year))

if __name__ == '__main__':
    main()

