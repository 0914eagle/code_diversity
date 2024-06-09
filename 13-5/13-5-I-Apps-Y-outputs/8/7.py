
import datetime

def get_day_of_week(date_string):
    date = datetime.datetime.strptime(date_string, '%d %m')
    return date.strftime('%A')

def main():
    date_string = input("Enter a date in the format DD MM: ")
    print(get_day_of_week(date_string))

if __name__ == '__main__':
    main()

