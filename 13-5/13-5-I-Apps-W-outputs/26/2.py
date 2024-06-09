
def solve(s):
    n = len(s)
    if n == 1:
        return "("
    if s[0] == "(":
        return "(" + solve(s[1:])
    else:
        return ")" + solve(s[1:])

