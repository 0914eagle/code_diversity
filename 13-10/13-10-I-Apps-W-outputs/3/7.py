
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
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]

def consecutive_months(days):
    years = []
    months = []
    current_year = 1900
    current_month = 1
    for day in days:
        days_in_month = get_days_in_month(current_month, current_year)
        if day <= days_in_month:
            months.append(current_month)
            days_in_month -= day
            if days_in_month == 0:
                current_month += 1
                if current_month == 13:
                    current_year += 1
                    current_month = 1
            break
        else:
            months.append(current_month)
            current_month += 1
            if current_month == 13:
                current_year += 1
                current_month = 1
            day -= days_in_month
    else:
        return False
    return True

def main():
    days = list(map(int, input().split()))
    print("Yes") if consecutive_months(days) else print("No")

if __name__ == '__main__':
    main()

