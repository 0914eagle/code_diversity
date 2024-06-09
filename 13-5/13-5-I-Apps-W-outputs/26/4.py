
def solve(s):
    n = len(s)
    if n == 1:
        return "(:("
    if s[0] == "(" and s[n-1] == ")":
        return "(()())"
    if s.count("(") == s.count(")"):
        return "(:("
    for i in range(n):
        if s[i] == "?":
            s = s[:i] + "(" + s[i+1:]
            break
    for i in range(n-1, -1, -1):
        if s[i] == "?":
            s = s[:i+1] + ")" + s[i+1:]
            break
    return s

