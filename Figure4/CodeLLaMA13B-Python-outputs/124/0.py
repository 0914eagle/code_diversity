def valid_date(date):
    
    if len(date) == 0:
        return False
    if date[2] != '-' or date[5] != '-':
        return False
    if date[0:2] > '12' or date[0:2] < '01':
        return False
    if date[3:5] > '31' or date[3:5] < '01':
        return False
    if date[0:2] == '02' and date[3:5] > '29':
        return False
    if date[0:2] in ['04', '06', '09', '11'] and date[3:5] > '30':
        return False
    if date[0:2] in ['01', '03', '05', '07', '08', '10', '12'] and date[3:5] > '31':
        return False
    return True


if __name__ == '__main__':
    print(valid_date('03-11-2000'))
    print(valid_date('15-01-2012'))
    print(valid_date('04-0-2040'))
    print(valid_date('06-04-2020'))
    print(valid_date('06/04/2020'))
