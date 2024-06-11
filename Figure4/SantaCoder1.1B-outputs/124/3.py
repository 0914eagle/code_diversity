def valid_date(date):
    
    if not date:
        return False
    if len(date) < 1:
        return False
    if len(date) > 31:
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
    if date.count('-') > 12 or date.count('/') > 12:
        return False
    if date.count('-') < 4 or date.count('/') < 4:
        return False
    if date.count('-') > 29 or date.count('/') > 29:
        return False
    if date.count('-') < 2 or date.count('/') < 2:
        return False
    if date.count('/') > 2:
        return False
    if date.count('/') < 1:
        return False
    if date.count('/') > 1:
        return False
    if date.count('/') == 1:
        if date.count('-') == 1:
            if date.count('/') == 1:
                if date[0] == '0':
                    return False
                if date[0] == '1':
                    return False
                if date[0] == '2':
                    return False
                if date[0] == '3':
                    return False
                if date[0] == '4':
                    return False
                if date[0] == '5':
                    return False
                if date[0] == '6':
                    return False
                if date[0] == '7':
                    return False
                if date[0] == '8':
                    return False
                if date[0] == '9':
                    return False
                if date[0] == '10':
                    return False
                if date[0] == '11':
                    return False
                if date[0] == '12':
                    return False
                if date[0] == '13':
                    return False
                if date[0] == '14':
                    return False
                if date[0] == '15':
                    return False
                if date[0] == '16':
                    return False
               