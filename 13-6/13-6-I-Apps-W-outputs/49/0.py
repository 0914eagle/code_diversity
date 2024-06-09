
def solve(a):
    n = len(a)
    s = [0] * n
    for i in range(n):
        if a[i] % 2 == 0:
            s[i] = "+"
        else:
            s[i] = "-"
    return "".join(s)

