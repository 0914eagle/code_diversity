
def solve(n, k, d, s):
    if k == 0:
        return "impossible"
    else:
        return round(d - (s - d) * k / (n - k), 6)

