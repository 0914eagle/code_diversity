def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if a.find(b) != -1:
        return True
    else:
        for i in range(1, len(b)):
            if a.find(b[i:] + b[:i]) != -1:
                return True
    return False

