
def solve(n, k, d, s):
    if s > d:
        return "impossible"
    else:
        return (d * (n - k) + s * k) / n

