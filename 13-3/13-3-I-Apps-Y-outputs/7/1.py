
def get_day_of_week(date):
    day, month = map(int, date.split())
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and day > days_in_month[month]:
        day = day % days_in_month[month]
    return "Monday" if (day + sum(days_in_month[:month]) + 2009) % 7 == 0 else "Tuesday" if (day + sum(days_in_month[:month]) + 2009) % 7 == 1 else "Wednesday" if (day + sum(days_in_month[:month]) + 2009) % 7 == 2 else "Thursday" if (day + sum(days_in_month[:month]) + 2009) % 7 == 3 else "Friday" if (day + sum(days_in_month[:month]) + 2009) % 7 == 4 else "Saturday" if (day + sum(days_in_month[:month]) + 2009) % 7 == 5 else "Sunday"

