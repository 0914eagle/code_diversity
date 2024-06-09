
def solve(s, k):
    n = len(s)
    for i in range(n):
        for j in range(i+1, min(n, i+k+1)):
            s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
    return s

