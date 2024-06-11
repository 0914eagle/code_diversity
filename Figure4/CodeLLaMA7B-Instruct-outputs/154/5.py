

def cycpattern_check(a , b):
    
    # Write your code here
    a = a.lower()
    b = b.lower()
    if b in a:
        return True
    else:
        for i in range(len(b)):
            if b[i:] + b[:i] in a:
                return True
    return False

