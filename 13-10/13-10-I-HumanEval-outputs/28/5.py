
def valid_date(date: str) -> bool:
    
    # Check if the date string is not empty
    if not date:
        return False

    # Check if the date is in the format mm-dd-yyyy
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False

    # Extract the month, day, and year from the date string
    month, day, year = date[:2], date[3:5], date[6:]

    # Check if the month is valid
    if not month.isdigit() or int(month) < 1 or int(month) > 12:
        return False

    # Check if the day is valid
    if not day.isdigit() or int(day) < 1:
        return False

    # Check if the year is valid
    if not year.isdigit() or len(year) != 4:
        return False

    # Check if the day is valid for the month
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) < 1 or int(day) > 31:
            return False
    elif int(month) in [4, 6, 9, 11]:
        if int(day) < 1 or int(day) > 30:
            return False
    elif int(month) == 2:
        if int(day) < 1 or int(day) > 29:
            return False

    # If all checks pass, return True
    return True

