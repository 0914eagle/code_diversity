
import datetime

def get_day_of_week(day, month):
    date = datetime.date(2009, month, day)
    return date.strftime("%A")

if __name__ == '__main__':
    day, month = map(int, input().split())
    print(get_day_of_week(day, month))

