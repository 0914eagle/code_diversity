
def solve(N, b):
    if N == 0:
        return "yes"
    if b == 0:
        return "no"
    if N > 10**15 or b > 50:
        return "no"
    return "yes"

