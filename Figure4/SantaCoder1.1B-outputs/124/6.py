def valid_date(date):
    
    if not date:
        return False
    if len(date) < 1:
        return False
    if len(date) > 31:
        return False
    if date[0] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return False
    if date[3] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return False
    if date[6] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return False
    if int(date[1]) < 1 or int(date[1]) > 12:
        return False
    if int(date[2]) < 1 or int(date[2]) > 31:
        return False
    if int(date[5]) < 1 or int(date[5]) > 30:
        return False
    if int(date[8]) < 1 or int(date[8]) > 29:
        return False
    return True


