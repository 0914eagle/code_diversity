def cycpattern_check(a , b):
    
    if len(a) != len(b):
        return False
    if len(a) == 0:
        return True
    if len(a) == 1:
        return a == b
    if len(a) == 2:
        return a == b or a[1:] == b[1:]
    if len(a) == 3:
        return a == b or a[1:] == b[1:] or a[2:] == b[2:]
    if len(a) == 4:
        return a == b or a[1:] == b[1:] or a[2:] == b[2:] or a[3:] == b[3:]
    if len(a) == 5:
        return a == b or a[1:] == b[1:] or a[2:] == b[2:] or a[3:] == b[3:] or a[4:] == b[4:]
    if len(a) == 6:
        return a == b or a[1:] == b[1:] or a[2:] == b[2:] or a[3:] == b[3:] or a[4:] == b[4:] or a[5:] == b[5:]
    if len(a) == 7:
        return a == b or a[1:] == b[1:] or a[2:] == b[2:] or a[3:] == b[3:] or a[4:] == b[4:] or a[5:] == b[5:] or a[6:] == b[6:]
    if len(a) == 8:
        return a == b or a[1:] == b[1:] or a[2:] == b[2:] or a[3:] == b[3:] or a[4:] == b[4:] or a[5:] == b[5:] or a[6:] == b[6:] or a[7:] == b[7:]
    if len(a) == 9:
        return a == b or a[1:] == b[1:] or a[2:] == b[2:] or a[3:] == b[3:] or a[4:] == b[4:] or a[5:] == b[5:] or a[6:] == b[6:] or a[7:] == b[7:]