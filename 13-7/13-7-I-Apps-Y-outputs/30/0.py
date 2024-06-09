
def solve(s, t):
    n = len(s)
    m = len(t)
    if m == 0:
        return n
    if m == 1:
        return n - 1 if s.count(t[0]) > 1 else n
    if m == n:
        return 0
    l, r = 0, m - 1
    while l < n and r < n and s[l] == t[0]:
        l += 1
    while r < n and s[r] == t[m - 1]:
        r += 1
    for i in range(l, r):
        if s[i] != t[i - l]:
            return n - r + 1
    return n - r + 1

