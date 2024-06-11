def cycpattern_check(a , b):
    
    if len(a) == 0 or len(b) == 0:
        return False
    if len(b) > len(a):
        return False
    if a == b:
        return True
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            return True
        elif a[i:] + a[:i] == b:
            return True
    return False


if __name__ == "__main