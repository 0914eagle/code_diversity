def valid_date(date):
    
    # your code here
    if date == '':
        return False
    if date[2] != '-' or date[5] != '-':
        return False
    if int(date[3:5]) < 1 or int(date[3:5]) > 12:
        return False
    if int(date[0:2]) == 2:
        if int(date[6:10]) % 4 == 0:
            if int(date[3:5]) > 29:
                return False
        else:
            if int(date[3:5]) > 28:
                return False
    if int(date[0:2]) in [1,3,5,7,8,10,12]:
        if int(date[3:5]) > 31:
            return False
    if int(date[0:2]) in [4,6,9,11]:
        if int(date[3:5]) > 30:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(valid_date('03-11-2000'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert valid_date('03-11-2000') == True
    assert valid_date('15-01-2012') == False
    assert valid_date('04-0-2040') == False
    assert valid_date('06-04-2020') == True
    assert valid_date('06/04/2020') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
