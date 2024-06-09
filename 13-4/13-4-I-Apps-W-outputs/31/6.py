
def is_friday(date, day_of_week):
    month, day = date.split()
    month = month.upper()
    day = int(day)
    day_of_week = day_of_week.upper()

    if month == "JAN" and day == 1:
        if day_of_week == "FRI":
            return "TGIF"
        else:
            return ":( "
    elif month == "FEB" and day == 29 and day_of_week == "FRI":
        return "TGIF"
    else:
        return ":( "

def main():
    date = input("Enter the date: ")
    day_of_week = input("Enter the day of the week: ")
    print(is_friday(date, day_of_week))

if __name__ == '__main__':
    main()

