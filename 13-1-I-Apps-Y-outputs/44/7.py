
def solve(N, K, X, Y):
    total = 0
    for i in range(1, N+1):
        if i <= K:
            total += X
        else:
            total += Y
    return total

