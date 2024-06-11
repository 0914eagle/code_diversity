def valid_date(date):
    
    if date == '':
        return False
    if len(date) < 1:
        return False
    if len(date) > 31:
        return False
    if len(date) > 12:
        return False
    if len(date) < 1:
        return False
    if date.count('-') != 2:
        return False
    if date.count('/') != 2:
        return False
    if date.count('-') < 1:
        return False
    if date.count('/') < 1:
        return False
    if date.count('-') > 3:
        return False
    if date.count('/') > 3:
        return False
    if date.count('-') < 1:
        return False
    if date.count('/') < 1:
        return False
    if date.count('-') > 3:
        return False
    if date.count('/') > 3:
        return False
    if date.count('-') < 1:
        return False
    if date.count('/') < 1:
        return False
    if date.count('-') > 3:
        return False
    if date.count('/') > 3:
        return False
    if date.count('-') < 1:
        return False
    if date.count('/') < 1:
        return False
    if date.count('-') > 3:
        return False
    if date.count('/') > 3:
        return False
    if date.count('-') < 1:
        return False
    if date.count('/') < 1:
        return False
    if date.count('-') > 3:
        return False
    if date.count('/') > 3:
        return False
    if date.count('-') < 1:
        return False
    if date.count('/') < 1:
        return False
    if date.count('-') > 3:
        return False
    if date.count('/') > 3:
        return False
    if date.count('-') < 1:
        return False
    if date.count('/') < 1:
        return False
    if date.count('-') > 3:
        return False
    if date.count('/') > 3:
        return False
    return True


