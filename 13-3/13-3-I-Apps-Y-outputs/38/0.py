
def get_min_value(N, K):
    while N != 0:
        N = abs(N - K)
    return N

