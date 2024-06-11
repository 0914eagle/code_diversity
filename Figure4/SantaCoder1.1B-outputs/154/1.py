def cycpattern_check(a , b):
    
    # Your code here
    a = a.lower()
    b = b.lower()
    if len(a) != len(b):
        return False
    if a == b:
        return True
    if len(a) == 1:
        return False
    if len(b) == 1:
        return False
    if a[0] == b[0]:
        return cycpattern_check(a[1:], b[1:])
    if a[-1] == b[-1]:
        return cycpattern_check(a[:-1], b[:-1])
    if a[-1] == b[0]:
        return cycpattern_check(a[:-1], b[1:])
    return False

