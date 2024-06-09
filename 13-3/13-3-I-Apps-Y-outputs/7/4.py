
def get_day_of_week(day, month):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_year = 0
    for i in range(month - 1):
        days_in_year += days_in_month[i]
    days_in_year += day
    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][days_in_year % 7]

