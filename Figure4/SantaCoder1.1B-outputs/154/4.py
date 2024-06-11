def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if len(a) == len(b):
        return a == b
    if len(a) == 1:
        return False
    if len(b) == 1:
        return False
    if a[0] == b[0]:
        return cycpattern_check(a[1:], b[1:])
    return False

