
import datetime

def is_halloween(date_string):
    month, day = date_string.split()
    month = int(datetime.datetime.strptime(month, "%b").month)
    day = int(day)
    if month == 10 and day == 31 or month == 12 and day == 25:
        return "yup"
    else:
        return "nope"

def main():
    date_string = input("Enter a date in the format FEB 9: ")
    print(is_halloween(date_string))

if __name__ == "__main__":
    main()

