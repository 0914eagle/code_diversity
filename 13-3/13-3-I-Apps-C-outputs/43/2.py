
def get_max_weights(weights, k, m):
    weights.sort()
    start = 0
    end = len(weights) - 1
    while start < end:
        if weights[start] + weights[end] == m:
            return k
        elif weights[start] + weights[end] < m:
            start += 1
        else:
            end -= 1
    return 0

