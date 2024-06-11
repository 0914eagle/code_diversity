def cycpattern_check(a , b):
    
    if len(a) == 0 or len(b) == 0:
        return False
    if len(a) < len(b):
        return False
    if len(a) == len(b):
        if a == b:
            return True
        else:
            return False
    else:
        for i in range(len(a)):
            if a[i:i+len(b)] == b:
                return True
        return False

