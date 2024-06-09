
def solve(s):
    n = len(s)
    for k in range(1, n+1):
        s_k = s[:k]
        if s_k == s_k[::-1]:
            return s_k, k
    return s, 1

