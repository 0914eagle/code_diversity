def valid_date(date):
    
    if not date:
        return False

    try:
        month, day, year = date.split('-')
    except ValueError:
        return False

    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False

    month, day, year = int(month), int(day), int(year)

    if month < 1 or month > 12:
        return False

    if day < 1:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    if month == 2 and day > 29:
        return False

    return True
