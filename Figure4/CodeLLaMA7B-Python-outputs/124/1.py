def valid_date(date):
    
    import re
    date_pattern = re.compile(r'^((0?[1-9])|(1[0-2]))\-(0?[1-9]|[12][0-9]|3[01])\-([12]\d{3})$')
    if date == '':
        return False
    else:
        date_match = date_pattern.match(date)
        if date_match:
            month = int(date_match.group(1))
            day = int(date_match.group(2))
            year = int(date_match.group(3))
            if month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32):
                return True
            elif month in [4, 6, 9, 11] and day in range(1, 31):
                return True
            elif month == 2 and day in range(1, 29):
                return True
            else:
                return False
        else:
            return False


