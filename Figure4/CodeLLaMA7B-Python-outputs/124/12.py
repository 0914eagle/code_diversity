def valid_date(date):
    
    # check if the date is empty
    if date == "":
        return False

    # check if the date is in the format mm-dd-yyyy
    if len(date) != 10:
        return False

    if date[2] != "-" or date[5] != "-":
        return False

    # check if the number of days is valid
    month = int(date[0:2])
    day = int(date[3:5])
    year = int(date[6:10])

    if month == 2:
        if day < 1 or day > 29:
            return False
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False

    # check if the month is valid
    if month < 1 or month > 12:
        return False

    # check if the year is valid
    if year < 0 or year > 9999:
        return False

    return True


print(valid_date("03-11-2000"))  # => True
print(valid_date("15-01-2012"))  # => False
print(valid_date("04-0-2040"))  # => False
print(valid_date("06-04-2020"))  # => True
print(valid_date("06/04/2020"))  # => False
