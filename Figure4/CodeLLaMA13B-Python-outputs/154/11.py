def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if len(a) == len(b):
        if a == b:
            return True
        else:
            return False
    if len(a) > len(b):
        for i in range(len(a)):
            if a[i:i+len(b)] == b:
                return True
            else:
                if a[i+1:i+len(b)+1] == b:
                    return True
                else:
                    if a[i+2:i+len(b)+2] == b:
                        return True
                    else:
                        if a[i+3:i+len(b)+3] == b:
                            return True
                        else:
                            return False

































































































































































































































































































































