
def get_max_weights(weights, k):
    total = sum(weights)
    for i in range(k):
        for j in range(i+1, k+1):
            if weights[i] + weights[j-1] == total // k:
                return k
    return k-1

