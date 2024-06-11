def cycpattern_check(a , b):
    
    if len(a) == len(b):
        return False
    if len(b) > len(a):
        return False
    if a in b:
        return True
    for i in range(len(b)):
        if b in a:
            return True
        a = a[1:] + a[0]
    return False


if __name__ == "__main__":
    print(cycpattern_check("abcd", "abd"))
    print(cycpattern_check