
def solve(s):
    n = len(s)
    t = [0] * n
    for i in range(n):
        t[i] = 1 - s[i]
    return "".join(map(str, t))

