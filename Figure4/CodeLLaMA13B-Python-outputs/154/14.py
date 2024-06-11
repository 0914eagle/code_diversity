def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    for i in range(len(b)):
        if a.find(b[i::]) != -1:
            return True
    return False


