
def cycpattern_check(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    double_a = a + a
    return b in double_a

# Test cases
print(cycpattern_check('abcd', 'abd'))
print(cycpattern_check('hello', 'ell'))
print(cycpattern_check('whassup', 'psus'))
print(cycpattern_check('abab', 'baa'))
print(cycpattern_check('efef', 'eeff'))
print(cycpattern_check('himenss', 'simen'))
