def valid_date(date):
    
    if not date:
        return False
    if not date.isdigit():
        return False
    if len(date) != 8:
        return False
    if date[2] != '-' or date[5] != '-':
        return False
    if int(date[0:2]) not in range(1, 13):
        return False
    if int(date[3:5]) not in range(1, 32):
        return False
    if int(date[6:]) not in range(1900, 2021):
        return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(valid_date('01-01-2000'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert valid_date('01-01-2000') == True
    assert valid_date('01-01-200') == False
    assert valid_date('01-01-20001') == False
    assert valid_date('01-01-20001') == False
    assert valid_date('01-01-10000') == False
    assert valid_date('01-01-100000') == False
    assert valid_date('01-01-1000000') == False
    assert valid_date('01-01-10000000') == False
    assert valid_date('01-01-100000000') == False
    assert valid_date('01-01-1000000000') == False
    assert valid_date('01-01-10000000000') == False
    assert valid_date('01-01-100000000000') == False
    assert valid_date('01-01-1000000000000') == False