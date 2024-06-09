
def solve(s, k):
    n = len(s)
    if k > n:
        return ""
    
    t = ""
    for i in range(k):
        t += min(s[i], key=s.index)
    
    return t

