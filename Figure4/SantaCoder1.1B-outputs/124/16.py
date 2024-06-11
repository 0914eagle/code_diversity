def valid_date(date):
    
    if not date:
        return False
    if len(date) < 1:
        return False
    if len(date) > 10:
        return False
    if date[0] not in '1234567890':
        return False
    if date[1] not in '1234567890':
        return False
    if date[2] not in '1234567890':
        return False
    if int(date[0:2]) < 1 or int(date[0:2]) > 12:
        return False
    if int(date[3:5]) < 1 or int(date[3:5]) > 31:
        return False
    if int(date[6:8]) < 1 or int(date[6:8]) > 30:
        return False
    if int(date[9:11]) < 1 or int(date[9:11]) > 29:
        return False
    return True


