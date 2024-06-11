def cycpattern_check(a , b):
    
    if a.find(b) != -1:
        return True
    else:
        for i in range(len(a)-1):
            a = a[1:] + a[0]
            if a.find(b) != -1:
                return True
    return False

