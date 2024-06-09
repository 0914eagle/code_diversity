
import datetime

def get_day_of_week(date):
    day, month = map(int, date.split())
    date_obj = datetime.date(2009, month, day)
    return date_obj.strftime("%A")

def main():
    date = input("Enter a date in the format D M: ")
    print(get_day_of_week(date))

if __name__ == '__main__':
    main()

