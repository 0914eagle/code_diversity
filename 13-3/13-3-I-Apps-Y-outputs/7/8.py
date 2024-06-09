
def get_day_of_week(date):
    day, month = map(int, date.split())
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_month_leap = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_passed = 0
    for m in range(1, month):
        if month == 2 and year % 4 == 0:
            days_passed += days_in_month_leap[m]
        else:
            days_passed += days_in_month[m]
    days_passed += day
    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][days_passed % 7]

