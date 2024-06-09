
def is_typo(s, t):
    n = len(s)
    if n != len(t):
        return 0
    
    count = 0
    for i in range(n):
        if s[i] != t[i]:
            count += 1
        if count > 1:
            return 0
    
    return count == 1

