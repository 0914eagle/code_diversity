def cycpattern_check(a , b):
    
    if len(a) == len(b):
        return False
    if len(a) > len(b):
        return cycpattern_check(b, a)
    for i in range(len(a)):
        if a[i:] + a[:i] == b:
            return True
    return False


if __name__ == "__main__":
    print(cycpattern_check("abcd", "abd"))
    print(cycpattern_check("hello", "ell"))
    print(cycpattern_check("whassup", "psus"))
    print(cycpattern_check("abab", "baa"))
    print(cycpattern_check("efef", "eeff"))
    print(cycpattern_check("himenss", "simen"))
