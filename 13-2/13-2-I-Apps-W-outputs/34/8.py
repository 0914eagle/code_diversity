
def solve(n, k):
    # Find the smallest x such that x div k * (x mod k) = n
    for x in range(1, 1001):
        if (x // k) * (x % k) == n:
            return x
    return -1

