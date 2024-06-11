def valid_date(date):
    
    if not date:
        return False
    if len(date) < 1:
        return False
    if len(date) > 30:
        return False
    if date.count('-') != 2:
        return False
    if date.count('/') != 2:
        return False
    if date.count('-') < 1 or date.count('/') < 1:
        return False
    if date.count('-') > 3 or date.count('/') > 3:
        return False
    if date.count('-') < 12 or date.count('/') < 12:
        return False
    if date.count('-') > 29 or date.count('/') > 29:
        return False
    if date.count('-') < 4 or date.count('/') < 4:
        return False
    if date.count('-') > 31 or date.count('/') > 31:
        return False
    if date.count('/') < 1 or date.count('/') > 12:
        return False
    if date.count('/') > 3:
        return False
    return True


