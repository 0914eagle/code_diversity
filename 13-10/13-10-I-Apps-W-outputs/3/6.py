
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(month, year):
    if month == 2:
        return 28 if not is_leap_year(year) else 29
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]

def can_form_months(days):
    days = days[:]
    months = []
    while days:
        month = days.pop(0)
        if month == 28:
            month = 29 if is_leap_year(year) else 28
        months.append(month)
        if not days:
            break
        days[0] -= month
        if days[0] < 0:
            return False
    return True

def solve(days):
    return "YES" if can_form_months(days) else "NO"

if __name__ == '__main__':
    num_days = int(input())
    days = [int(x) for x in input().split()]
    print(solve(days))

