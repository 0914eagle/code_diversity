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
    print(