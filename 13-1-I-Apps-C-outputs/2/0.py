
def is_possible(n, k, q, s):
    if k == 0:
        return "YES"
    
    if n == 1:
        return "NO"
    
    if k == 1:
        if s == q:
            return "NO"
        else:
            return "YES"
    
    if k > 1:
        if s == q:
            return "NO"
        else:
            return is_possible(n-1, k-1, q, s)


