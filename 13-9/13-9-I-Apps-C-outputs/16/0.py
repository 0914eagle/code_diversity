
def find_largest_base(y, l):
    for b in range(y, 10):
        if all(int(i) in range(0, 10) for i in str(y)) and int(str(y), b) >= l:
            return b
    return -1

