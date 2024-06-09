
def crackers(n, k):
    min_diff = float('inf')
    for i in range(1, n+1):
        diff = abs(i - n//k)
        min_diff = min(min_diff, diff)
    return min_diff

