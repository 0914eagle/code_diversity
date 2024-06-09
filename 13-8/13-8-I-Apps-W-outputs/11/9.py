
def get_optimal_subsequence(a, k, pos):
    # Find the maximum sum of a subsequence of length k
    max_sum = 0
    for i in range(len(a) - k + 1):
        sum = 0
        for j in range(k):
            sum += a[i + j]
        if sum > max_sum:
            max_sum = sum
            optimal_subsequence = a[i:i+k]
    # Return the value at the given position in the optimal subsequence
    return optimal_subsequence[pos - 1]
