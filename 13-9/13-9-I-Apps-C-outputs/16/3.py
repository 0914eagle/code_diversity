
def solve(y, l):
    for b in range(y, 10**18+1):
        if len(str(bin(b)[2:])) >= l:
            return b
    return -1

