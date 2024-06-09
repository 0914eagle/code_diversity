
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
            return n * (m - 1)
    
    if k == 4:
        if n == m:
            return (n - 1) * m - 1
        else:
            return n * (m - 1) - 1
    
    if k == 5:
        if n == m:
            return (n - 2) * m
        else:
            return n * (m - 2)
    
    if k == 6:
        if n == m:
            return (n - 2) * m - 1
        else:
            return n * (m - 2) - 1
    
    if k == 7:
        if n == m:
            return (n - 3) * m
        else:
            return n * (m - 3)
    
    if k == 8:
        if n == m:
            return (n - 3) * m - 1
        else:
            return n * (m - 3) - 1
    
    if k == 9:
        if n == m:
            return (n - 4) * m
        else:
            return n * (m - 4)
    
    if k == 10:
        if n == m:
            return (n - 4) * m - 1
        else:
            return n * (m - 4) - 1
    
    if k == 11:
        if n == m:
            return (n - 5) * m
        else:
            return n * (m - 5)
    
    if k == 12:
        if n == m:
            return (n - 5) * m - 1
        else:
            return n * (m - 5) - 1
    
    if k == 13:
        if n == m:
            return (n - 6) * m
        else:
            return n * (m - 6)
    
    if k == 14:
        if n == m:
            return (n - 6) * m - 1
        else:
            return n * (m - 6) - 1
    
    if k == 15:
        if n == m:
            return (n - 7) * m
        else:
            return n * (m - 7)
    
    if k == 16:
        if n == m:
            return (n - 7) * m - 1
        else:
            return n * (m - 7) - 1
    
    if k == 17:
        if n == m:
            return (n - 8) * m
        else:
            return n * (m - 8)
    
    if k == 18:
        if n == m:
            return (n - 8) * m - 1
        else:
            return n * (m - 8) - 1
    
    if k == 19:
        if n == m:
            return (n - 9) * m
        else:
            return n * (m - 9)
    
    if k == 20:
        if n == m:
            return (n - 9) * m - 1
        else:
            return n * (m - 9) - 1
    
    return -1

