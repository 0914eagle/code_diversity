def valid_date(date):
    
    if not date:
        return False
    if len(date) < 1:
        return False
    if len(date) > 31:
        return False
    if not re.match(r'^\d{1,2}-\d{1,2}-\d{4}$', date):
        return False
    if len(date.split('-')) != 3:
        return False
    if int(date.split('-')[0]) < 1 or int(date.split('-')[0]) > 12:
        return False
    if int(date.split('-')[1]) < 1 or int(date.split('-')[1]) > 31:
        return False
    if int(date.split('-')[2]) < 1 or int(date.split('-')[2]) > 30:
        return False
    if int(date.split('-')[0]) == 2 and int(date.split('-')[1]) == 29:
        return False
    if int(date.split('-')[0]) == 4 and int(date.split('-')[1]) == 6:
        return False
    if int(date.split('-')[0]) == 6 and int(date.split('-')[1]) == 9:
        return False
    if int(date.split('-')[0]) == 9 and int(date.split('-')[1]) == 11:
        return False
    return True


