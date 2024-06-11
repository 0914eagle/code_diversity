def cycpattern_check(a , b):
    
    if a == b:
        return True
    if len(a) != len(b):
        return False
    a = a + a
    return b in a


if __name__ == "__main__":
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True
