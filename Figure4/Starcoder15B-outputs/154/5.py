def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if len(a) == len(b):
        return a == b
    if len(a) == 1:
        return False
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            return True
    return False

