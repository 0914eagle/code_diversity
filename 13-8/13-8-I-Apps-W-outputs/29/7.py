
def get_min_steps(n, k):
    if k == 0:
        return 0
    if n < k:
        return k - n
    else:
        return n - k

