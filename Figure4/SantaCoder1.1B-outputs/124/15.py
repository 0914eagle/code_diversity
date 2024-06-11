def valid_date(date):
    
    if not date:
        return False
    if len(date) < 1:
        return False
    if len(date) > 10:
        return False
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return False
    if not re.match(r'^\d{1,2}$', date[0]):
        return False
    if not re.match(r'^\d{1,2}$', date[1]):
        return False
    if not re.match(r'^\d{4}$', date[2]):
        return False
    if int(date[0]) > 12:
        return False
    if int(date[1]) > 31:
        return False
    if int(date[2]) > 29:
        return False
    if int(date[0]) == 1:
        if int(date[1]) == 1 or int(date[1]) == 3 or int(date[1]) == 5 or int(date[1]) == 7 or int(date[1]) == 8 or int(date[1]) == 10 or int(date[1]) == 12:
            return False
        if int(date[1]) == 4 or int(date[1]) == 6 or int(date[1]) == 9 or int(date[1]) == 11:
            return False
    if int(date[0]) == 4:
        if int(date[1]) == 6 or int(date[1]) == 9 or int(date[1]) == 11:
            return False
    if int(date[0]) == 6:
        if int(date[1]) == 9 or int(date[1]) == 11:
            return False
    if int(date[0]) == 9:
        if int(date[1]) == 11:
            return False
    if int(date[0]) == 11:
        return False
    return True


