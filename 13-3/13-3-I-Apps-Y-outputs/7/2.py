
def get_day_of_week(date):
    day, month = map(int, date.split())
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_year = 0
    for m in range(month):
        days_in_year += days_in_month[m]
    days_in_year += day
    return "Monday" if days_in_year % 7 == 1 else \
           "Tuesday" if days_in_year % 7 == 2 else \
           "Wednesday" if days_in_year % 7 == 3 else \
           "Thursday" if days_in_year % 7 == 4 else \
           "Friday" if days_in_year % 7 == 5 else \
           "Saturday" if days_in_year % 7 == 6 else \
           "Sunday"

