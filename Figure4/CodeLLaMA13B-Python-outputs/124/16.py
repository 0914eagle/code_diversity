def valid_date(date):
    
    if date == '':
        return False
    if len(date) != 10:
        return False
    if date[2] != '-' or date[5] != '-':
        return False
    if int(date[0:2]) not in range(1, 13):
        return False
    if int(date[3:5]) not in range(1, 32):
        return False
    if int(date[6:10]) not in range(1, 2021):
        return False
    return True


print(valid_date('03-11-2000'))
print(valid_date('15-01-2012'))
print(valid_date('04-0-2040'))
print(valid_date('06-04-2020'))
print(valid_date('06/04/2020'))
