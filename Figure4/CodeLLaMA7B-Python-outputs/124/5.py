def valid_date(date):
    
    if len(date) == 0:
        return False
    date_list = date.split('-')
    if len(date_list) != 3:
        return False
    month = int(date_list[0])
    day = int(date_list[1])
    year = int(date_list[2])
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return False
        if month in [4, 6, 9, 11]:
            if day > 30:
                return False
        if month == 2:
            if day > 29:
                return False
    return True


if __name__ == '__main__':
    print(valid_date('03-11-2000'))
    print(valid_date('15-01-2012'))
    print(valid_date('