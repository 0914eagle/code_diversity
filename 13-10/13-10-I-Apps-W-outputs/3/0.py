
def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 28 if not is_leap_year(year) else 29
    else:
        return 30

def check_consecutive_months(n, a):
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    days_left = a.copy()
    for i in range(n):
        month = months[i]
        year = i // 12 + 1
        days_in_month = get_days_in_month(month, year)
        if days_in_month != days_left[0]:
            return "NO"
        days_left = days_left[1:]
    return "YES"

def main():
    n, a = get_input()
    print(check_consecutive_months(n, a))

if __name__ == '__main__':
    main()

