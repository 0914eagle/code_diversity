
def solve(s, k):
    n = len(s)
    if k > n:
        return "-1"
    
    t = ""
    for i in range(k):
        t += min(s[i:])
        s = s.replace(t[i], "")
    
    return t

