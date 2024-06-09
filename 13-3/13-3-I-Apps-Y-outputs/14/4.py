
def solve(N, b):
    if N == 0:
        return "yes"
    if b == 0:
        return "no"
    if N > (2**b) - 1:
        return "no"
    return "yes"

