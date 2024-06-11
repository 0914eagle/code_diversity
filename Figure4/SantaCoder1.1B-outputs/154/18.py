def cycpattern_check(a , b):
    
    a = a.lower()
    b = b.lower()
    if len(a) != len(b):
        return False
    if len(a) == 0:
        return True
    if a == b:
        return True
    if a[0] != b[0]:
        return False
    for i in range(1, len(a)):
        if a[i] != b[i-1] and a[i] != b[i+1]:
            return False
    return True

