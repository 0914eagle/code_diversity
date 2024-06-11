

def cycpattern_check(a , b):
    
    a_list = list(a)
    b_list = list(b)
    b_rotated = b_list[1:] + b_list[:1]
    if b in a:
        return True
    for i in range(len(b_rotated)):
        if b_rotated[i] in a:
            return True
    return False

