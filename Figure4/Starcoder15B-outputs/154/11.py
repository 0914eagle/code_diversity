def cycpattern_check(a , b):
    
    if a.find(b) != -1:
        return True
    else:
        for i in range(len(b)):
            if a.find(b[i:]) + a.find(b[:i]) != -2:
                return True
        return False

