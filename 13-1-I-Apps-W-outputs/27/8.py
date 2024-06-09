
def solve(a, b, c, n):
    if a + b + c != n:
        return -1
    if a + b < c or b + c < a or a + c < b:
        return -1
    return n - a - b - c

