
def find_min_steps(n, k):
    if k == 0:
        return 0
    else:
        return max(abs(n - k), abs(n + k))

