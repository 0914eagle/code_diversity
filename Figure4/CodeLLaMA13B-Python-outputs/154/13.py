def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if len(a) == len(b):
        if a == b:
            return True
        else:
            return False
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            return True
        else:
            if a[i:i+len(b)] == b[1:]+b[0]:
                return True
            elif a[i:i+len(b)] == b[2:]+b[0]+b[1]:
                return True
            elif a[i:i+len(b)] == b[3:]+b[0]+b[1]+b[2]:
                return True
    return False


print(cycpattern_check("abcd","abd"))
print(cycpattern_check("hello","ell"))
print(cycpattern_check("whassup","psus"))
print(cycpattern_check("abab","baa"))
print(cycpattern_check("efef","eeff"))
print(cycpattern_check("himenss","simen"))
