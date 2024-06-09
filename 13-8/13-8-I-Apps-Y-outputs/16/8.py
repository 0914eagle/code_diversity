
def solve(N, K):
    probabilities = []
    for i in range(1, N+1):
        if i >= K:
            probabilities.append(1)
        else:
            probabilities.append(i * (1/2)**i)
    return sum(probabilities)

