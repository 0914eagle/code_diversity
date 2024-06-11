def valid_date(date):
    
    if not date:
        return False
    try:
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month not in range(1, 13):
            return False
        if day not in range(1, 32):
            return False
        if month in [1, 3, 5, 7, 8, 10, 12] and day not in range(1, 32):
            return False
        if month in [4, 6, 9, 11] and day not in range(1, 31):
            return False
        if month == 2 and day not in range(1, 29):
            return False
        return True
    except:
        return False


print(valid_date('03-11-2000'))
print(valid_date('15-01-2012'))
print(valid_date('04-0-2040'))
print(valid_date('06-04-2020'))
print(valid_date('06/04/2020'))
