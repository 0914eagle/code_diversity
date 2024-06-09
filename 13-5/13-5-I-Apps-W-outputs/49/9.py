
def solve(s):
    n = len(s)
    for i in range(n-1):
        if s[i] == '?':
            s = s[:i] + 'a' + s[i+1:]
        elif s[i+1] == '?':
            s = s[:i+1] + 'a' + s[i+2:]
        elif s[i] == s[i+1]:
            return "-1"
    return s

