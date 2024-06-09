
def solve(s):
    n = len(s)
    if n == 1:
        return "(:"
    for i in range(n):
        if s[i] == "?":
            s = s[:i] + "(" + s[i+1:]
    for i in range(n-1):
        if s[i] == "(" and s[i+1] == "(":
            return "(:"
    return s

