

def cycpattern_check(a , b):
    
    a_list = list(a)
    b_list = list(b)
    b_rotations = []
    for i in range(len(b)):
        b_rotations.append(b_list[i:]+b_list[:i])
    for i in range(len(b_rotations)):
        if b_rotations[i] in a_list:
            return True
    return False

