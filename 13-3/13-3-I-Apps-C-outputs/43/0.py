
def get_max_weights(weights, k):
    total = sum(weights)
    for i in range(1, k+1):
        for subset in combinations(weights, i):
            if sum(subset) == total // k:
                return i
    return 0

