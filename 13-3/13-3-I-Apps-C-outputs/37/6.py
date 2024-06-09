
def get_max_area(n, m, k):
    if k == 0:
        return n * m
    
    if k == 1:
        return max(n, m)
    
    if k == 2:
        return n * m - min(n, m)
    
    if k == 3:
        if n == m:
            return n * m - n
        else:
            return n * m - min(n, m)
    
    if k == 4:
        if n == m:
            return n * m - n * 2
        else:
            return n * m - min(n, m) * 2
    
    if k == 5:
        if n == m:
            return n * m - n * 3
        else:
            return n * m - min(n, m) * 3
    
    if k == 6:
        if n == m:
            return n * m - n * 4
        else:
            return n * m - min(n, m) * 4
    
    if k == 7:
        if n == m:
            return n * m - n * 5
        else:
            return n * m - min(n, m) * 5
    
    if k == 8:
        if n == m:
            return n * m - n * 6
        else:
            return n * m - min(n, m) * 6
    
    if k == 9:
        if n == m:
            return n * m - n * 7
        else:
            return n * m - min(n, m) * 7
    
    if k == 10:
        if n == m:
            return n * m - n * 8
        else:
            return n * m - min(n, m) * 8
    
    return -1

