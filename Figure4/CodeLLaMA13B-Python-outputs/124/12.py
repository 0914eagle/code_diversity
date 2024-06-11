def valid_date(date):
    
    if not date:
        return False
    if not date.isdigit():
        return False
    if len(date) != 8:
        return False
    if date[2] != '-' or date[5] != '-':
        return False
    if int(date[0:2]) < 1 or int(date[0:2]) > 12:
        return False
    if int(date[3:5]) < 1 or int(date[3:5]) > 31:
        return False
    if int(date[0:2]) in [1,3,5,7,8,10,12] and int(date[3:5]) > 31:
        return False
    if int(date[0:2]) in [4,6,9,11] and int(date[3:5]) > 30:
        return False
    if int(date[0:2]) == 2 and int(date[3:5]) > 29:
        return False
    return True
