def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    for i in range(len(b)):
        if b in a:
            return True
        else:
            a = a[1:] + a[0]
    return False

