def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if a == b:
        return True
    for i in range(len(b)):
        if a[i:].find(b) != -1:
            return True
    return False


if __name__ == "__main__":
    print(cycpattern_check("abcd", "abd"))
    print(cycpattern_check("hello", "ell"))
    print(cycpattern_check("whassup", "