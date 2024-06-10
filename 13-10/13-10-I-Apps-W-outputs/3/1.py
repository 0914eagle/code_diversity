
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_month_days(month, year):
    if month == 2:
        return 28 if not is_leap_year(year) else 29
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]

def consecutive_months(days, years):
    months = []
    for year in years:
        for month in range(1, 13):
            if days[0] <= get_month_days(month, year):
                months.append(month)
                days[0] -= get_month_days(month, year)
                if len(days) == 1:
                    return True
                break
    return False

def main():
    n = int(input())
    days = list(map(int, input().split()))
    years = list(range(1, n + 1))
    print("YES") if consecutive_months(days, years) else print("NO")

if __name__ == '__main__':
    main()

