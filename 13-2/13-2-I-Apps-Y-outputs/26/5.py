
def solve(n):
    for x in range(1, n+1):
        k = 1
        while 2**k * x <= n:
            if 2**k * x == n:
                return x
            k += 1
    return -1

