def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if len(a) == len(b):
        return a == b
    if len(a) > len(b):
        for i in range(len(b)):
            if a.find(b) != -1:
                return True
            a = a[1:] + a[0]
        return False


if