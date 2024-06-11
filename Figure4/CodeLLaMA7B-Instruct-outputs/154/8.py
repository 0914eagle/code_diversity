

def cycpattern_check(a , b):
    
    a = list(a)
    b = list(b)
    if b in a:
        return True
    else:
        for i in range(len(b)):
            b.append(b.pop(0))
        if b in a:
            return True
        else:
            return False

