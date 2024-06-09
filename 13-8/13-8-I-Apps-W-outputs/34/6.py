
def solve(s):
    n = len(s)
    for k in range(1, n+1):
        if s[:k] == s[:k][::-1]:
            return s, k
    return s, 1

