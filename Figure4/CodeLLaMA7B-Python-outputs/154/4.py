def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if len(b) == 0:
        return True
    if len(b) == 1:
        return a.find(b) != -1
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            return True
        if a[i:i+len(b)] == b[::-1]:
            return True
    return False


if __name__ == "__main__":
    input_string = "abcde"
    input_string