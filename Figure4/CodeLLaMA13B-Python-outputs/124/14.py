def valid_date(date):
    
    if len(date) == 0:
        return False
    month, day, year = date.split('-')
    if int(month) not in range(1, 13):
        return False
    if int(day) not in range(1, 32):
        return False
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) not in range(1, 32):
            return False
    if int(month) in [4, 6, 9, 11]:
        if int(day) not in range(1, 31):
            return False
    if int(month) == 2:
        if int(day) not in range(1, 29):
            return False
    return True


print(valid_date('03-11-2000'))
print(valid_date('15-01-2012'))
print(valid_date('04-0-2040'))
print(valid_date('06-04-2020'))
print(valid_date('06/04/2020'))
