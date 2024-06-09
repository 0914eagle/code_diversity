
def get_max_sum(a, b, k):
    n = len(a)
    if k >= n:
        return sum(a) + sum(b)
    if k == 0:
        return 0
    a = sorted(a)
    b = sorted(b)
    max_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + b[j] > max_sum:
                max_sum = a[i] + b[j]
    return max_sum

