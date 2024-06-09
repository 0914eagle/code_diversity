
def solve(s):
    n = len(s)
    for i in range(n-1):
        if s[i] == '?':
            for j in 'abc':
                if s[i+1] != j:
                    s = s[:i] + j + s[i+1:]
                    break
            else:
                return "-1"
    return s

