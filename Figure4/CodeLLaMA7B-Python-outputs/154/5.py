def cycpattern_check(a , b):
    
    if len(a) == len(b):
        return False
    if len(a) < len(b):
        return False
    if a == b:
        return False
    if a.find(b) != -1:
        return True
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if a.find(rotated_b) != -1:
            return True
    return False


if __name__ == '__main__':
    print(cycpattern_check("abcd", "abd"))
