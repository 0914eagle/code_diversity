
def solve(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1, n):
            if s[i:j] == s[:j] + s[j:]:
                return i+1, j
    return -1, -1

