
def get_day_of_week(date):
    day, month = date.split()
    day = int(day)
    if month == "JAN":
        return "MON"
    elif month == "FEB":
        return "TUE"
    elif month == "MAR":
        return "WED"
    elif month == "APR":
        return "THU"
    elif month == "MAY":
        return "FRI"
    elif month == "JUN":
        return "SAT"
    elif month == "JUL":
        return "SUN"
    elif month == "AUG":
        return "MON"
    elif month == "SEP":
        return "TUE"
    elif month == "OCT":
        return "WED"
    elif month == "NOV":
        return "THU"
    else:
        return "FRI"

def is_friday(date, day_of_week):
    day, month = date.split()
    day = int(day)
    if month == "FEB" and day == 29:
        return "not sure"
    elif day_of_week == "FRI":
        return "TGIF"
    else:
        return ":"

if __name__ == '__main__':
    date = input()
    day_of_week = get_day_of_week(date)
    print(is_friday(date, day_of_week))

