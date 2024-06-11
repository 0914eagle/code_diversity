def valid_date(date):
    
    if not date:
        return False

    try:
        month, day, year = date.split('-')
    except ValueError:
        return False

    if not 1 <= int(month) <= 12:
        return False

    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if not 1 <= int(day) <= 31:
            return False
    elif int(month) in [4, 6, 9, 11]:
        if not 1 <= int(day) <= 30:
            return False
    elif int(month) == 2:
        if not 1 <= int(day) <= 29:
            return False

    return True


if __name__ == '__main__':
    print("Example:")
    print(valid_date('01-01-2000'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert valid_date('01-01-2000') == True
    assert valid_date('04-0-2040') == False
    assert valid_date('06-04-2020') == True
    assert valid_date('06/04/2020') == False
    assert valid_date('02-29-2000') == False
    assert valid_date('02-29-2001') == True
    assert valid_date('02-29-2004') == False
    assert valid_date('02-29-2008') == True
    assert valid_date('02-29-1900') == False
    assert valid_date('02-30-2000') == False
    assert valid_date('02-31-2000') == False
    assert valid_date('02-30-2001') == False
    assert valid_date('02-31-2001') == False
   