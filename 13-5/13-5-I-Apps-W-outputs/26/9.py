
def solve(s):
    n = len(s)
    if n == 1:
        return "(:("
    prefixes = [""]
    for i in range(n):
        if s[i] == "?":
            prefixes.append(s[:i+1])
    for i in range(n):
        if s[i] == "?":
            s = s[:i] + "(" + s[i+1:]
            if is_correct(s):
                return s
            s = s[:i] + ")" + s[i+1:]
            if is_correct(s):
                return s
    return "(:("

def is_correct(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

