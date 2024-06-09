
def solve(s):
    n = len(s)
    if n == 1:
        return "(:"
    if s[0] == "?":
        return solve(s[1:])
    if s[n-1] == "?":
        return solve(s[:n-1])
    if s.count("(") != s.count(")"):
        return "(:"
    for i in range(n):
        if s[i] == "?":
            s = s[:i] + "(" + s[i+1:]
            break
    return solve(s)

