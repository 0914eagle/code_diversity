
def get_min_time(a, b, w, x, c):
    if c <= a:
        return 0
    if b >= x:
        return c - a
    else:
        return c - a - 1 + w - (x - b)

