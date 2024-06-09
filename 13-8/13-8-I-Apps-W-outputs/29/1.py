
def get_min_steps(n, k):
    if k == 0:
        return 0
    else:
        return max(n - k, k)

