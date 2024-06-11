def valid_date(date):
    
    if not date:
        return False
    if len(date) == 0:
        return False
    if len(date) > 10:
        return False
    if len(date) < 10:
        return False
    if not date.isdigit():
        return False
    if int(date[0]) > 12:
        return False
    if int(date[3]) > 31:
        return False
    if int(date[5]) > 30:
        return False
    if int(date[7]) > 29:
        return False
    if int(date[8]) > 31:
        return False
    if int(date[10]) > 30:
        return False
    if int(date[12]) > 29:
        return False
    if int(date[1]) < 1 or int(date[3]) < 1 or int(date[5]) < 1 or int(date[7]) < 1 or int(date[8]) < 1 or int(date[10]) < 1 or int(date[12]) < 1:
        return False
    return True


