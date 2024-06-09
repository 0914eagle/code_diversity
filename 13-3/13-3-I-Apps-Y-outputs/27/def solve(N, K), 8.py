
def solve(N, K):
    while N != 0:
        N = abs(N - K)
    return N

