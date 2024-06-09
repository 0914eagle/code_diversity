
def solve(a, k, pos):
    # find the maximum sum of a subsequence of length k
    max_sum = 0
    for i in range(len(a) - k + 1):
        sum = 0
        for j in range(k):
            sum += a[i + j]
        if sum > max_sum:
            max_sum = sum

    # find the lexicographically minimal subsequence of length k with the maximum sum
    min_subsequence = []
    for i in range(len(a) - k + 1):
        sum = 0
        for j in range(k):
            sum += a[i + j]
        if sum == max_sum:
            subsequence = a[i:i+k]
            if len(min_subsequence) == 0 or subsequence < min_subsequence:
                min_subsequence = subsequence

    return min_subsequence[pos - 1]

