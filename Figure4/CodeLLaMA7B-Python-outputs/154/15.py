def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if a == b:
        return True
    for i in range(len(b)):
        if a[i:i+len(b)] == b:
            return True
        if a[i:] + a[:i] == b:
            return True
    return False


if __name__ == "__main__":
    input_string = "abcde"
    input_string2 = "abd"