def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if a == b:
        return True
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            return True
    return False

