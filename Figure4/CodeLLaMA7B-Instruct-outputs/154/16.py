

def cycpattern_check(a , b):
    
    # Your code here
    b_rotations = [b[i:] + b[:i] for i in range(len(b))]
    if b in a or any(b_rotation in a for b_rotation in b_rotations):
        return True
    else:
        return False

