def valid_date(date):
    
    if not date:
        return False
    try:
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month < 1 or month > 12:
            return False
        if day < 1:
            return False
        if month in [1,3,5,7,8,10,12] and day > 31:
            return False
        if month in [4,6,9,11] and day > 30:
            return False
        if month == 2 and day > 29:
            return False
    except:
        return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(valid_date('01-01-2000'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert valid_date('01-01-2000') == True
    assert valid_date('01-01-1000') == True
    assert valid_date('01-01-0001') == True
    assert valid_date('00-00-0000') == False
    assert valid_date('12-31-2000') == True
    assert valid_date('12-31-2001') == True
    assert valid_date('12-31-9999') == True
    assert valid_date('12-32-2000') == False
    assert valid_date('12-31-1999') == False
    assert valid_date('13-01-2000') == False
    assert valid_date('00-00-1000') == False
    assert valid_date('01-01-1001') == False
    assert valid_date('00-00-0001') == False
    assert valid_date('01-01-100') == False
    assert