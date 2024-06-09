
def get_day_of_week(day, month):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == "FEB" and day == 29:
        return "FRI"
    for i in range(1, month):
        day += days_in_month[i]
    return "FRI" if day % 7 == 0 else "NOT FRI"

def get_year(day, month, year):
    if month == "FEB" and day == 29 and year % 4 == 0:
        return "TGIF"
    return "NOT FRI"

def main():
    day, month = map(int, input().split())
    day_of_week = get_day_of_week(day, month)
    year = get_year(day, month, int(input()))
    if day_of_week == "FRI":
        print("TGIF")
    elif year == "TGIF":
        print("TGIF")
    else:
        print(":(")

if __name__ == '__main__':
    main()

