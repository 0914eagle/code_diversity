
def get_input():
    n = int(input())
    days = list(map(int, input().split()))
    return n, days

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_month_days(month, year):
    if month == 2:
        return 28 if not is_leap_year(year) else 29
    return 30 if month in [4, 6, 9, 11] else 31

def consecutive_months(n, days):
    months = [0] * 12
    month = 0
    year = 0
    for i in range(n):
        days_in_month = get_month_days(month, year)
        if days[i] <= days_in_month:
            months[month] += days[i]
            days_in_month -= days[i]
        else:
            months[month] += days_in_month
            days[i] -= days_in_month
            month = (month + 1) % 12
            year += month // 12
    return all(months)

def main():
    n, days = get_input()
    print("YES" if consecutive_months(n, days) else "NO")

if __name__ == '__main__':
    main()

