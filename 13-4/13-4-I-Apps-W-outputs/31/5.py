
def is_friday(day, month):
    if month == "JAN":
        if day == 1 or day == 8 or day == 15 or day == 22 or day == 29:
            return "TGIF"
        else:
            return "not sure"
    elif month == "FEB":
        if day == 1 or day == 8 or day == 15 or day == 22:
            return "TGIF"
        else:
            return "not sure"
    elif month == "MAR":
        if day == 1 or day == 8 or day == 15 or day == 22 or day == 29:
            return "TGIF"
        else:
            return "not sure"
    elif month == "APR":
        if day == 1 or day == 8 or day == 15 or day == 22:
            return "TGIF"
        else:
            return "not sure"
    elif month == "MAY":
        if day == 1 or day == 8 or day == 15 or day == 22 or day == 29:
            return "TGIF"
        else:
            return "not sure"
    elif month == "JUN":
        if day == 1 or day == 8 or day == 15 or day == 22 or day == 29:
            return "TGIF"
        else:
            return "not sure"
    elif month == "JUL":
        if day == 1 or day == 8 or day == 15 or day == 22 or day == 29:
            return "TGIF"
        else:
            return "not sure"
    elif month == "AUG":
        if day == 1 or day == 8 or day == 15 or day == 22 or day == 29:
            return "TGIF"
        else:
            return "not sure"
    elif month == "SEP":
        if day == 1 or day == 8 or day == 15 or day == 22 or day == 29:
            return "TGIF"
        else:
            return "not sure"
    elif month == "OCT":
        if day == 1 or day == 8 or day == 15 or day == 22 or day == 29:
            return "TGIF"
        else:
            return "not sure"
    elif month == "NOV":
        if day == 1 or day == 8 or day == 15 or day == 22 or day == 29:
            return "TGIF"
        else:
            return "not sure"
    elif month == "DEC":
        if day == 1 or day == 8 or day == 15 or day == 22 or day == 29:
            return "TGIF"
        else:
            return "not sure"
    else:
        return "not sure"

def main():
    day, month = input().split()
    day = int(day)
    month = month.upper()
    result = is_friday(day, month)
    print(result)

if __name__ == '__main__':
    main()

