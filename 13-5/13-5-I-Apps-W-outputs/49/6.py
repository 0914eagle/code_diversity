
def solve(s):
    n = len(s)
    for i in range(n-1):
        if s[i] == s[i+1]:
            return "-1"
    return s

