
def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def find_next_leap_year(year):
    while True:
        year += 1
        if is_leap_year(year):
            return year

def solve(year):
    next_leap_year = find_next_leap_year(year)
    return next_leap_year

if __name__ == '__main__':
    year = int(input())
    print(solve(year))

