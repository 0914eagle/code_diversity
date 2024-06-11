def cycpattern_check(a , b):
    
    if len(a) != len(b):
        return False
    if len(a) == 0:
        return True
    if a == b:
        return True
    if a == b[::-1]:
        return True
    if a == b[1:-1]:
        return True
    return False


