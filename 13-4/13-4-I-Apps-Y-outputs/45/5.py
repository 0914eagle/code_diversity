
def kangaroo_jump(x):
    # Find the earliest possible time to reach coordinate X
    # by jumping to the right or left with a length of 1, 2, 3, ..., x
    for i in range(1, x+1):
        if x % i == 0:
            return i
    return -1

