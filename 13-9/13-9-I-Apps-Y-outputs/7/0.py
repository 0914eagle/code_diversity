
def get_min_diff(n, k):
    min_diff = float('inf')
    for i in range(1, n+1):
        min_diff = min(min_diff, abs(i - (n%k)))
    return min_diff

