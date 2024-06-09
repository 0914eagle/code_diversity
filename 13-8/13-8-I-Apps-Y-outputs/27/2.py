
def solve(n, k, d, s):
    if k == 0:
        return "impossible"
    else:
        return round(d - (d-s)*(k/n), 6)

