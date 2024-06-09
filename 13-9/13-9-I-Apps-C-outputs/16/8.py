
def find_largest_base(y, l):
    for b in range(y, 10**18):
        if all(int(digit) in range(10) for digit in str(y)) and int(y, b) >= l:
            return b
    return -1

