def cycpattern_check(a , b):
    
    if len(a) != len(b):
        return False
    if len(a) == 0:
        return True
    if a == b:
        return True
    if a[0] == b[0]:
        return cycpattern_check(a[1:], b[1:])
    return False

