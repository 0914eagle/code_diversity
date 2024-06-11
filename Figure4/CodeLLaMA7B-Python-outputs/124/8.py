def valid_date(date):
    
    if len(date) == 0:
        return False
    month, day, year = date.split('-')
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) < 1 or int(day) > 31:
            return False
    elif int(month) in [4, 6, 9, 11]:
        if int(day) < 1 or int(day) > 30:
            return False
    elif int(month) == 2:
        if int(day) < 1 or int(day) > 29:
            return False
    if int(month) < 1 or int(month) > 12:
        return False
    return True


if __name__ == '__main__':
    print(valid_date('03-11-2000'))
    print(valid_date('15-01-2012'))
    print(valid_date('04-0-2040'))
    print(valid_date('06-04-2020'))
    print(valid_date('06/04/2020'))
