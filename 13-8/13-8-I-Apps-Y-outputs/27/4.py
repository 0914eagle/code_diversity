
def get_average_difficulty(n, k, d, s):
    if k == 0:
        return "impossible"
    else:
        return (d * (n - k) + s * k) / n

