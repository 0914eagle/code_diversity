
def solve(s):
    n = len(s)
    if n == 0:
        return "()"
    if s[0] == "?":
        return "(" + solve(s[1:])
    if s[0] == "(":
        return "(" + solve(s[1:]) + ")"
    if s[0] == ")":
        return ")" + solve(s[1:])
    return "(" + solve(s[1:]) + ")"

