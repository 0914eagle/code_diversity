
def solve(y, ell):
    for b in range(y, 10**18):
        if all(int(i) in range(10) for i in str(y)) and int(str(y), b) >= ell:
            return b
    return -1

