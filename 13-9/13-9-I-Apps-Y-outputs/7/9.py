
def solve(N, K):
    crackers = [1] * K
    for i in range(N):
        crackers[i % K] += 1
    return max(crackers) - min(crackers)

