
import datetime

def get_day_of_week(day, month):
    date = datetime.date(2009, month, day)
    return date.strftime("%A")

def main():
    day, month = map(int, input("Enter day and month: ").split())
    print(get_day_of_week(day, month))

if __name__ == '__main__':
    main()

