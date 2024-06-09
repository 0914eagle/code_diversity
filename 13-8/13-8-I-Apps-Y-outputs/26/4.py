
def solve(H, n, d):
    for i in range(n):
        H += d[i]
        if H <= 0:
            return i+1
    return -1

