def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            return True
        if a[i:i+len(b)] == b[len(b)-1:] + b[:len(b)-1]:
            return True
        if a[i:i+len(b)] == b[1:] + b[0]:
            return True
    return False


print(cycpattern_check("abcd","abd"))
print(cycpattern_check("hello","ell"))
print(cycpattern_check("whassup","psus"))
print(cycpattern_check("abab","baa"))
print(cycpattern_check("efef","eeff"))
print(cycpattern_check("himenss","simen"))
