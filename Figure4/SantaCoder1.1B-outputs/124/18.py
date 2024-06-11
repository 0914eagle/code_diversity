def valid_date(date):
    
    if not date:
        return False
    if len(date) == 0:
        return False
    if len(date) > 10:
        return False
    if len(date) < 10:
        return False
    if date.count('-') != 2:
        return False
    if date.count('/') != 2:
        return False
    if date.count('-') < 1 or date.count('/') < 1:
        return False
    if date.count('-') > 31 or date.count('/') > 31:
        return False
    if date.count('-') < 12 or date.count('/') < 12:
        return False
    if date.count('-') > 29 or date.count('/') > 29:
        return False
    if date.count('-') < 4 or date.count('/') < 4:
        return False
    if date.count('-') > 6 or date.count('/') > 6:
        return False
    if date.count('-') < 9 or date.count('/') < 9:
        return False
    if date.count('-') > 11 or date.count('/') > 11:
        return False
    if date.count('/') < 2:
        return False
    if date.count('/') > 3:
        return False
    if date.count('/') < 1:
        return False
    if date.count('/') > 12:
        return False
    return True


