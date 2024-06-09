
def solve(N, K):
    probabilities = []
    for i in range(1, N+1):
        if i < K:
            probabilities.append(1/N)
        else:
            probabilities.append(0)
    return sum(probabilities)

