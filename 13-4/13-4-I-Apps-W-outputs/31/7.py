
def get_day_of_week(date):
    day, month = date.split()
    day = int(day)
    if month == "JAN":
        return (day + 1) % 7
    elif month == "FEB":
        return (day + 2) % 7
    elif month == "MAR":
        return (day + 3) % 7
    elif month == "APR":
        return (day + 4) % 7
    elif month == "MAY":
        return (day + 5) % 7
    elif month == "JUN":
        return (day + 6) % 7
    elif month == "JUL":
        return (day + 0) % 7
    elif month == "AUG":
        return (day + 1) % 7
    elif month == "SEP":
        return (day + 2) % 7
    elif month == "OCT":
        return (day + 3) % 7
    elif month == "NOV":
        return (day + 4) % 7
    elif month == "DEC":
        return (day + 5) % 7

def get_day_of_week_from_newspaper(day):
    if day == "MON":
        return 0
    elif day == "TUE":
        return 1
    elif day == "WED":
        return 2
    elif day == "THU":
        return 3
    elif day == "FRI":
        return 4
    elif day == "SAT":
        return 5
    elif day == "SUN":
        return 6

def is_friday(date, day_of_week_from_newspaper):
    day_of_week = get_day_of_week(date)
    if day_of_week == 4:
        return True
    elif day_of_week == 5 and day_of_week_from_newspaper == 4:
        return True
    else:
        return False

def main():
    date = input("Enter the date: ")
    day_of_week_from_newspaper = input("Enter the day of the week on 1 January: ")
    if is_friday(date, get_day_of_week_from_newspaper(day_of_week_from_newspaper)):
        print("TGIF")
    else:
        print(":(")

if __name__ == '__main__':
    main()

