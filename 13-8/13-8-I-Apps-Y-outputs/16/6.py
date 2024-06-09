
def get_probability(N, K):
    probability = 0
    for i in range(1, N+1):
        if i < K:
            probability += 1/N
        else:
            probability += 1/N * (1/2)**(i-1)
    return probability

