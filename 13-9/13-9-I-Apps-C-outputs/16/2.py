
def solve(y, l):
    for b in range(y, 10**18+1):
        if all(int(c) >= 0 and int(c) <= 9 for c in str(y)) and int(str(y), b) >= l:
            return b
    return -1

