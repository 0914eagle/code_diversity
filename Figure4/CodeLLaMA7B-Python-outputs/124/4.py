def valid_date(date):
    
    import re
    import datetime
    date_pattern = re.compile(r'^(\d{1,2})-(\d{1,2})-(\d{4})$')
    match = date_pattern.search(date)
    if match:
        month, day, year = match.groups()
        if int(month) in range(1, 13) and int(day) in range(1, 32) and int(year) > 0:
            try:
                datetime.date(int(year), int(month), int(day))
                return True
            except ValueError:
                return False
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    print(valid_date('03-11-2000'))
    print(valid_date('15-01-2012'))
    print(valid_date('04-0-2040'))
    print(valid_date('06-04-2020'))
    print(valid_date('