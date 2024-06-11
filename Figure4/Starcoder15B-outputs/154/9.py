def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if b in a:
        return True
    for i in range(len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False

