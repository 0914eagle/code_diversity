
def get_max_weights(weights, k, m):
    weights.sort()
    start = 0
    end = len(weights) - k
    max_weights = 0
    while start < end:
        curr_sum = sum(weights[start:start+k])
        if curr_sum == m:
            max_weights = max(max_weights, k)
            start += 1
        elif curr_sum < m:
            start += 1
        else:
            end -= 1
    return max_weights

