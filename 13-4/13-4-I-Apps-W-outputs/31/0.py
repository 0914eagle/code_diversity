
import datetime

def get_day_of_week(date):
    day, month = date.split()
    day = int(day)
    month = datetime.datetime.strptime(month, "%b").month
    year = datetime.datetime.now().year
    return datetime.datetime(year, month, day).strftime("%a")

def is_friday(day_of_week):
    if day_of_week == "FRI":
        return "TGIF"
    elif day_of_week == "SAT" or day_of_week == "SUN":
        return "not sure if today might be Friday, depending on if this year has a 29th of February"
    else:
        return ":("

def main():
    date = input()
    day_of_week = get_day_of_week(date)
    print(is_friday(day_of_week))

if __name__ == '__main__':
    main()

