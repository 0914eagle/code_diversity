
def solve(N, K):
    probability = 0
    for i in range(1, N+1):
        if i < K:
            probability += 1 / (N*N)
        elif i == K:
            probability += 1 / N
    return probability

