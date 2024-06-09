
def get_max_weights(weights, k, m):
    weights.sort()
    start = 0
    end = len(weights) - k
    max_weights = 0
    while start < end:
        curr_sum = sum(weights[start:start+k])
        if curr_sum == m:
            max_weights = max(max_weights, k)
        if curr_sum > m:
            end -= 1
        else:
            start += 1
    return max_weights

