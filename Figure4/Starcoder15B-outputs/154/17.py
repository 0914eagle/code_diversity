def cycpattern_check(a , b):
    
    if a.find(b) != -1:
        return True
    else:
        for i in range(len(a)):
            if a[i:]+a[:i] == b:
                return True
        return False

