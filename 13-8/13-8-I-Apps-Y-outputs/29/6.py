
def get_max_sum(a, b, k):
    n = len(a)
    if k >= n:
        return sum(a) + sum(b)
    if k == 0:
        return 0
    a.sort()
    b.sort()
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, a[i] + b[n-i-1])
    return max_sum

