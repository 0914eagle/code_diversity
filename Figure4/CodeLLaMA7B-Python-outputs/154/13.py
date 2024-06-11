def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if len(b) == 0:
        return True
    if len(a) == 0:
        return False
    if len(b) == 1:
        return b in a
    if a == b:
        return True
    if a.find(b) != -1:
        return True
    for i in range(len(b)):
        if a.find(b[i:] + b[:i]) != -1:
            return True
    return False


if