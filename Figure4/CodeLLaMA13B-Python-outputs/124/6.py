def valid_date(date):
    
    if not date:
        return False
    if len(date) != 10:
        return False
    if date[2] != '-' or date[5] != '-':
        return False
    if date[6:].isdigit() == False or date[:2].isdigit() == False:
        return False
    if int(date[3:5]) > 12 or int(date[3:5]) < 1:
        return False
    if int(date[0:2]) > 31 or int(date[0:2]) < 1:
        return False
    if int(date[3:5]) in [4, 6, 9, 11] and int(date[0:2]) > 30 or int(date[3:5]) in [1, 3, 5, 7, 8, 10, 12] and int(date[0:2]) > 31:
        return False
    if int(date[3:5]) == 2 and int(date[0:2]) > 29:
        return False
    return True


print(valid_date('03-11-2000'))
print(valid_date('15-01-2012'))
print(valid_date('04-0-2040'))
print(valid_date('06-04-2020'))
print(valid_date('06/04/2020'))
