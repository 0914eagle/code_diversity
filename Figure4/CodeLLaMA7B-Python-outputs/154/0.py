def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if len(b) == 0:
        return True
    if a == b:
        return True
    if len(b) == 1:
        return a.find(b) != -1
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            return True
        if a[i:i+len(b)] == a[0:len(b)]:
            return cycpattern_check(a[i+1:],b)
    return False


if __name