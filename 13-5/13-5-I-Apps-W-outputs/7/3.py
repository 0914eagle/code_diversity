
def solve(s, t):
    if s == t:
        return "both"
    if len(s) != len(t):
        return "need tree"
    
    # suffix automaton
    for i in range(len(s)):
        if s[i] != t[i]:
            s = s[:i] + s[i+1:]
            break
    
    # suffix array
    for i in range(len(s)):
        if s[i] != t[i]:
            s = s[:i] + t[i] + s[i+1:]
            break
    
    if s == t:
        return "array"
    else:
        return "need tree"

