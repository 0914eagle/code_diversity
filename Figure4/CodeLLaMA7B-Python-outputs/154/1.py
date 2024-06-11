def cycpattern_check(a , b):
    
    if len(a) == len(b):
        return False
    if len(a) < len(b):
        return False
    if len(b) == 0:
        return False
    if len(a) == 0:
        return False
    if len(b) == 1:
        return False
    if len(a) == 1:
        return False

    for i in range(len(b)):
        if a.find(b) != -1:
            return True
        else:
            b = b[-1] + b[:-1]
    return False


