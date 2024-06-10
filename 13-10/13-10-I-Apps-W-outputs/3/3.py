
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_month_days(month, year):
    if month == 2:
        return 28 if not is_leap_year(year) else 29
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]

def is_sequence_of_months(days, months):
    if len(days) != len(months):
        return False
    year = 2000
    month = 1
    day = 1
    for i in range(len(days)):
        month_days = get_month_days(month, year)
        if days[i] > month_days - day:
            return False
        day += days[i]
        month += 1
        if month == 13:
            month = 1
            year += 1
    return True

def main():
    n = int(input())
    days = list(map(int, input().split()))
    months = list(map(int, input().split()))
    print("YES" if is_sequence_of_months(days, months) else "NO")

if __name__ == '__main__':
    main()

