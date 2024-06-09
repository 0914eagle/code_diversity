
def solve(a, c):
    n = len(a)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + a[i]
    min_sum = float('inf')
    for i in range(c - 1, n):
        min_sum = min(min_sum, prefix_sums[i + 1] - prefix_sums[i - c + 2])
    return min_sum

