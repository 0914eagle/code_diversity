
def max_area(n, m, k):
    if k == 0:
        return n * m
    
    if k == 1:
        return max(n, m)
    
    if k == 2:
        return n * m - min(n, m)
    
    if k == 3:
        if n == m:
            return (n - 1) * m
        else:
            return n * m - min(n, m)
    
    if k == 4:
        if n == m:
            return (n - 2) * m
        else:
            return n * m - 2 * min(n, m) + 1
    
    if k == 5:
        if n == m:
            return (n - 3) * m
        else:
            return n * m - 3 * min(n, m) + 2
    
    if k == 6:
        if n == m:
            return (n - 4) * m
        else:
            return n * m - 4 * min(n, m) + 3
    
    if k == 7:
        if n == m:
            return (n - 5) * m
        else:
            return n * m - 5 * min(n, m) + 4
    
    if k == 8:
        if n == m:
            return (n - 6) * m
        else:
            return n * m - 6 * min(n, m) + 5
    
    if k == 9:
        if n == m:
            return (n - 7) * m
        else:
            return n * m - 7 * min(n, m) + 6
    
    if k == 10:
        if n == m:
            return (n - 8) * m
        else:
            return n * m - 8 * min(n, m) + 7
    
    return -1

