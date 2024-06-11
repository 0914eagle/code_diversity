def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if len(a) == len(b):
        return a == b
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            return True
        if a[i:i+len(b)] == b[::-1]:
            return True
    return False


