def cycpattern_check(a , b):
    
    if len(a) != len(b):
        return False
    if len(a) == 0:
        return True
    if len(a) == 1:
        return False
    if len(a) == 2:
        return a == b
    if len(a) == 3:
        return a == b or a == b[::-1]
    if len(a) == 4:
        return a == b or a == b[::-1] or a == b[1:] + b[:-1]
    if len(a) == 5:
        return a == b or a == b[::-1] or a == b[1:] + b[:-1] or a == b[2:] + b[1:-1]
    if len(a) == 6:
        return a == b or a == b[::-1] or a == b[1:] + b[:-1] or a == b[2:] + b[1:-1] or a == b[3:] + b[2:-1]
    if len(a) == 7:
        return a == b or a == b[::-1] or a == b[1:] + b[:-1] or a == b[2:] + b[1:-1] or a == b[3:] + b[2:-1] or a == b[4:] + b[3:-1]
    if len(a) == 8:
        return a == b or a == b[::-1] or a == b[1:] + b[:-1] or a == b[2:] + b[1:-1] or a == b[3:] + b[2:-1] or a == b[4:] + b[3:-1] or a == b[5:] + b[4:-1]
    if len(a) == 9:
        return a == b or a == b[::-1] or a == b[1:] + b[:-1] or a == b[2:] + b[1:-1] or a == b[3:] + b[2:-1] or a == b[4:] + b[3:-1] or a == b[5:] + b[4:-1] or a == b[6:] + b[5:-1]
    if len(a) == 10:
        return a == b or a == b[::-