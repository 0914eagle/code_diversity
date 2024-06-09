
def solve(N, b):
    if N == 0:
        return "yes"
    if b == 0:
        return "no"
    if N > 100000000000000:
        return "no"
    if b > 50:
        return "no"
    return "yes"

