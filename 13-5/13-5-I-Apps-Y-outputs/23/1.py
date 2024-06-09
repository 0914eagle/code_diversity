
import datetime

def is_halloween(date_string):
    month, day = date_string.split()
    month = month.upper()
    day = int(day)
    if month == "OCT" and day == 31:
        return "yup"
    elif month == "DEC" and day == 25:
        return "yup"
    else:
        return "nope"

def main():
    date_string = input("Enter a date in the format MMM DD: ")
    print(is_halloween(date_string))

if __name__ == '__main__':
    main()

