
def solve(s, k):
    n = len(s)
    for i in range(n):
        for j in range(i+1, min(i+k+1, n)):
            s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
    return s

