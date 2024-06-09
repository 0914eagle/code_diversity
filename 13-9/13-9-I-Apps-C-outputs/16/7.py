
def solve(y, ell):
    for b in range(y, 10):
        if str(y).isdigit() and int(str(y), b) >= ell:
            return b
    return -1

