
def solve(y, l):
    for b in range(y, 100):
        if len(str(y)) == len(str(int(y, b))):
            return b
    return -1

