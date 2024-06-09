
def solve(y, ell):
    for b in range(10, 11):
        if str(y).isdigit() and int(str(y), b) >= ell:
            return b
    return -1

