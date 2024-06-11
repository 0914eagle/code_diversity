def cycpattern_check(a , b):
    
    if len(a) == len(b):
        return False
    if len(b) > len(a):
        return False
    if a == b:
        return True
    if a.find(b) != -1:
        return True
    for i in range(len(b)):
        if a.find(b[i:] + b[:i]) != -1:
            return True
    return False


if __name__ == "__main__":
    input_string = "abcde"
    input_string2 = "cde"
    print(cycpattern_check(input_string, input_string2))
