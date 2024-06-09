
def solve(N, K):
    min_diff = float('inf')
    for i in range(1, N+1):
        diff = abs(i - N%K)
        if diff < min_diff:
            min_diff = diff
    return min_diff

