
def solve(s, t):
    if s == t:
        return "automaton"
    if len(s) != len(t):
        return "tree"
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i+1:] == t[i+1:]:
                return "array"
            if s[:i] + s[i+1:] == t[:i] + t[i+1:]:
                return "automaton"
    return "both"

