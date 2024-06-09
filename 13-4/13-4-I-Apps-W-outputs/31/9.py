
import datetime

def get_current_date():
    return datetime.date.today()

def get_day_of_week(date):
    return date.strftime("%a")

def is_friday(date):
    return get_day_of_week(date) == "FRI"

def main():
    date = get_current_date()
    day_of_week = get_day_of_week(date)
    if is_friday(date):
        print("TGIF")
    else:
        print(":(")

if __name__ == '__main__':
    main()

