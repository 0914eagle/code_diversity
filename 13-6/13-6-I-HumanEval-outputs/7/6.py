
def valid_date(date: str) -> bool:
    
    date_parts = date.split('-')
    if len(date_parts) != 3:
        return False
    month, day, year = date_parts
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False
    if int(month) < 1 or int(month) > 12:
        return False
    if int(day) < 1:
        return False
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) > 31:
            return False
    elif int(month) in [4, 6, 9, 11]:
        if int(day) > 30:
            return False
    elif int(month) == 2:
        if int(day) > 29:
            return False
    return True

