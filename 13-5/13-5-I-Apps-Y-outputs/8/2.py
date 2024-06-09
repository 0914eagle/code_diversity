
import datetime

def get_day_of_week(date):
    return datetime.datetime.strptime(date, "%d %m").strftime("%A")

def main():
    date = input("Enter a date in the format DD MM: ")
    print(get_day_of_week(date))

if __name__ == '__main__':
    main()

