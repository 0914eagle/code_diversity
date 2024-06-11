def valid_date(date):
    
    if not date:
        return False
    if len(date) < 1:
        return False
    if len(date) > 10:
        return False
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return False
    if re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        date = date.split('-')
        if len(date) != 3:
            return False
        if int(date[0]) < 1 or int(date[0]) > 12:
            return False
        if int(date[1]) < 1 or int(date[1]) > 31:
            return False
        if int(date[2]) < 1 or int(date[2]) > 30:
            return False
    return True


