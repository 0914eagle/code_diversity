
def solve(N, K):
    probability = 0
    for i in range(1, N+1):
        if i < K:
            probability += 1 / (3 ** (K-i))
    return probability

