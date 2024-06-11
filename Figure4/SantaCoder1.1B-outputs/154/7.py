def cycpattern_check(a , b):
    
    a = a.lower()
    b = b.lower()
    if len(a) != len(b):
        return False
    if len(a) == 0:
        return True
    if len(a) == 1:
        return a == b
    if len(a) == 2:
        return a == b or a + b == b + a
    if len(a) == 3:
        return a == b or a + b == b + a + b
    if len(a) == 4:
        return a == b or a + b == b + a + b + b
    if len(a) == 5:
        return a == b or a + b == b + a + b + b + b
    if len(a) == 6:
        return a == b or a + b == b + a + b + b + b + b
    if len(a) == 7:
        return a == b or a + b == b + a + b + b + b + b + b
    if len(a) == 8:
        return a == b or a + b == b + a + b + b + b + b + b + b + b
    if len(a) == 9:
        return a == b or a + b == b + a + b + b + b + b + b + b + b + b + b
    if len(a) == 10:
        return a == b or a + b == b + a + b + b + b + b + b + b + b + b + b + b + b + b
    if len(a) == 11:
        return a == b or a + b == b + a + b + b + b + b + b + b + b + b + b + b + b + b + b + b
    if len(a) == 12:
        return a == b or a + b == b + a + b + b + b + b + b + b + b + b + b + b + b + b + b + b + b + b
    if len(a) == 13:
        return a == b or a + b == b + a + b + b + b + b + b + b + b + b + b + b + b + b + b + b + b