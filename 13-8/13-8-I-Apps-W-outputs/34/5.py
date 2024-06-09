
def solve(s):
    n = len(s)
    for k in range(1, n+1):
        ss = s[::-1]
        if ss < s:
            return ss, k
    return s, 1

