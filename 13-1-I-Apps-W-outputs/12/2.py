
def is_friday(date, day_of_week):
    today = date.split()
    month = today[1]
    day = int(today[0])
    if month == "JAN" and day == 1:
        if day_of_week == "FRI":
            return "TGIF"
        else:
            return "not sure"
    elif month == "FEB" and day == 29:
        return "not sure"
    else:
        return "not Friday"

