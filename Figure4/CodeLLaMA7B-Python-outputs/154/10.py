def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if len(b) == 0:
        return True
    if len(b) == 1:
        return a.find(b) != -1
    if len(b) > len(a):
        return False
    if a.find(b) != -1:
        return True
    for i in range(len(b)):
        if a.find(b[i:] + b[:i]) != -1:
            return True
    return False


if __name__ == "__main__":
    print(cycpattern_check("abcd", "abd"))
    print(cycpattern_check("hello", "ell"))
    print(cycpattern_check("whassup", "psus"))
    print(cycpattern_check("abab", "baa"))
    print(cycpattern_check("efef", "eeff"))
    print(cycpattern_check("himenss", "simen"))
