
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

def get_friday(day_of_week, year):
    if day_of_week == 5:
        return "TGIF"
    elif day_of_week == 6 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return "TGIF"
    else:
        return ":( "

def main():
    date = input("Enter the date (DD MM): ")
    day_of_week = get_day_of_week(date)
    year = int(input("Enter the year: "))
    friday = get_friday(day_of_week, year)
    print(friday)

if __name__ == '__main__':
    main()

