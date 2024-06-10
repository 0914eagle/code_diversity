
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def get_days_in_month(month, year):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return [31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]

def can_represent_months(days):
    months = [0] * 12
    months[0] = days[0]
    for i in range(1, len(days)):
        months[i] = months[i - 1] + days[i]
        if months[i] > get_days_in_month(i + 1, 2000):
            return False
    return True

def main():
    n = int(input())
    days = list(map(int, input().split()))
    print("YES") if can_represent_months(days) else print("NO")

if __name__ == '__main__':
    main()

