
def solve(N, K):
    import math
    return math.factorial(N) // math.factorial(N - K) % (2**31 - 1)

