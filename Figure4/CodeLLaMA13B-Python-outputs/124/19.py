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
    if month not in range(1, 13) or day not in range(1, 32) or year not in range(1, 10001):
        return False
    if month in [1, 3, 5, 7, 8, 10, 12] and day not in range(1, 32):
        return False
    if month in [4, 6, 9, 11] and day not in range(1, 31):
        return False
    if month == 2 and day not in range(1, 29):
        return False
    return True
