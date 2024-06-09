
def solve(n, k, d, s):
    if k == 0:
        return "impossible"
    else:
        return round(d * (n - k) / k + s, 6)

