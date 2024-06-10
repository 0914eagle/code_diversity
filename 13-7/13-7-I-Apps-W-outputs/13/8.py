
def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def find_next_leap_year(year):
    while True:
        year += 1
        if is_leap_year(year):
            return year

def find_next_same_calendar(year):
    while True:
        year = find_next_leap_year(year)
        if year % 4 == 0:
            return year

def main():
    year = int(input())
    print(find_next_same_calendar(year))

if __name__ == '__main__':
    main()

