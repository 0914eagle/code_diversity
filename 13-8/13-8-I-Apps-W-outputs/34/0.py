
def solve(s):
    n = len(s)
    for k in range(1, n+1):
        for i in range(n-k+1):
            s = s[:i] + s[i:i+k][::-1] + s[i+k:]
    return s, k

