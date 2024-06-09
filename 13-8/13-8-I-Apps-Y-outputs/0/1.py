
def solve(abcc):
    a, b, c = map(int, input().split())
    return str(min(a + b, a + c, b + c))

