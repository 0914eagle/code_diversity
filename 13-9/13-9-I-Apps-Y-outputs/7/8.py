
def solve(n, k):
    min_diff = n // k
    extra_crackers = n % k
    for i in range(extra_crackers):
        min_diff = min(min_diff, i + 1)
    return min_diff

