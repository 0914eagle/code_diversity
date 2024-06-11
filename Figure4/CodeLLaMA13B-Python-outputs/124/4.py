def valid_date(date):
    
    if len(date) == 0:
        return False
    try:
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if month in [1,3,5,7,8,10,12] and day > 31:
            return False
        if month in [4,6,9,11] and day > 30:
            return False
        if month == 2 and day > 29:
            return False
        return True
    except:
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert valid_date('03-11-2000'), "First"
    assert valid_date('15-01-2012'), "Second"
    assert not valid_date('04-0-2040'), "Third"
    assert valid_date('06-04-2020'), "Fourth"
    assert not valid_date('06/04/2020'), "Fifth"
    print('"Run" is good. How is "Check"?')
