def valid_date(date):
    
    if len(date) == 0:
        return False
    try:
        month, day, year = date.split('-')
        if int(month) in range(1, 13) and int(day) in range(1, 32) and int(year) > 0:
            if int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) in range(1, 32):
                return True
            elif int(month) in [4, 6, 9, 11] and int(day) in range(1, 31):
                return True
            elif int(month) == 2 and int(day) in range(1, 29):
                return True
            else:
                return False
        else:
            return False
    except:
        return False


if __name__ == '__main__':
    print(valid_date('03-11-2000'))
    print(valid_date('15-01-2012'))
    print(valid_date('04-0-2040'))
    print(valid_date('06-04-2020'))
    print(valid_date('06/04/2020'))
