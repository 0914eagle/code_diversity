
def valid_date(date: str) -> bool:
    
    # Check if the date string is not empty
    if not date:
        return False

    # Check if the date is in the format mm-dd-yyyy
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False

    # Extract the month, day, and year from the date string
    month = int(date[:2])
    day = int(date[3:5])
    year = int(date[6:])

    # Check if the month is valid
    if month < 1 or month > 12:
        return False

    # Check if the day is valid based on the month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if day < 1 or day > 29:
            return False
    else:
        return False

    # Check if the year is valid
    if year < 0 or year > 9999:
        return False

    # If all checks pass, the date is valid
    return True

