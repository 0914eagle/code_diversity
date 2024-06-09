
def get_day_of_week(day, month):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and day > days_in_month[month]:
        day = day - days_in_month[month]
        month = month + 1
    if month > 2 and day > days_in_month[month]:
        day = day - days_in_month[month]
        month = month + 1
    if month == 12:
        month = 0
    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][day % 7]

