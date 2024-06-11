def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i:i+len(b)] == b:
                return True
            else:
                a = a[1:] + a[0]
        return False


if __name__ == '__main__':
    print(cycpattern_check("abcd","