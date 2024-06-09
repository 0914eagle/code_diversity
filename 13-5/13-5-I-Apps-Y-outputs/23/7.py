
import datetime

def is_halloween(date_str):
    month, day = date_str.split()
    month = month.upper()
    day = int(day)
    if month == "OCT" and day == 31:
        return "yup"
    elif month == "DEC" and day == 25:
        return "yup"
    else:
        return "nope"

def main():
    date_str = input("Enter a date in the format FEB 9: ")
    print(is_halloween(date_str))

if __name__ == '__main__':
    main()

