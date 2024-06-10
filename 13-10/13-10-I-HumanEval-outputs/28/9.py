
def valid_date(date: str) -> bool:
    

    # Check if the date string is not empty
    if not date:
        return False

    # Check if the date is in the format mm-dd-yyyy
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False

    # Check if the month is valid
    month = int(date[:2])
    if month < 1 or month > 12:
        return False

    # Check if the day is valid
    day = int(date[3:5])
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
    year = int(date[6:])
    if year < 0 or year > 9999:
        return False

    return True

