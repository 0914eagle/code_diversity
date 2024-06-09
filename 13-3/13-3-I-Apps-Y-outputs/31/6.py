
def solve(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j] and s[i:j+1] in s:
                return i+1, j+1
    return -1, -1

