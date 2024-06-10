
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(month, year):
    if month == 2:
        return 28 if not is_leap_year(year) else 29
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]

def solve(days):
    days_left = days
    year = 1
    month = 1
    while days_left > 0:
        days_in_month = get_days_in_month(month, year)
        if days_left < days_in_month:
            return "NO"
        days_left -= days_in_month
        month += 1
        if month == 13:
            month = 1
            year += 1
    return "YES"

if __name__ == '__main__':
    n = int(input())
    days = list(map(int, input().split()))
    print(solve(days))

