def cycpattern_check(a , b):
    
    if len(a) == len(b):
        return False
    if len(a) < len(b):
        return False
    if len(b) == 0:
        return False
    if len(a) == 0:
        return False

    if b in a:
        return True
    else:
        for i in range(len(b)):
            if b in a[i:]:
                return True

    return False


if __name__ == "__main__":
    print(cycpattern_check("abcd", "abd"))
    print(cycpattern_check("hello", "ell"))
    print(cycpattern_check("whassup", "psus"))
    print(cycpattern_check("abab", "baa"))
    print(cycpattern_check("efef", "eeff"))
    print(cycpattern_check("himenss", "simen"))
