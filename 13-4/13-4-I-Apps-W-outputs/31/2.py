
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
    else:
        return (day + 5) % 7

def is_friday(date, day_of_week):
    if day_of_week == 4:
        return "TGIF"
    else:
        return "not sure"

def main():
    date = input("Enter the date: ")
    day_of_week = get_day_of_week(date)
    print(is_friday(date, day_of_week))

if __name__ == '__main__':
    main()

