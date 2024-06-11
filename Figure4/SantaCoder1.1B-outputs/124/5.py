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
    if int(date[0]) > 12:
        return False
    if int(date[1]) > 31:
        return False
    if int(date[2]) > 29:
        return False
    if int(date[0]) < 1:
        return False
    if int(date[1]) < 1:
        return False
    if int(date[2]) < 1:
        return False
    if int(date[0]) > 31:
        return False
    if int(date[1]) > 30:
        return False
    if int(date[2]) > 29:
        return False
    return True

