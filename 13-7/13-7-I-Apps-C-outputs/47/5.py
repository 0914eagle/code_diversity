
def solve(n, k, s, t):
    c = 0
    for i in range(n):
        if s[i] == t[i]:
            c += 1
        else:
            break
    return c

