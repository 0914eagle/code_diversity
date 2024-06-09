
def is_friday(date, day_of_week):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month, day = date.split()
    month = months.index(month) + 1
    day = int(day)
    weekday = days_of_week.index(day_of_week)
    if month == 2 and day == 29 and weekday == 4:
        return "TGIF"
    if day == days_in_month[month - 1] and weekday == 4:
        return "TGIF"
    return ":("

months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
days_of_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

