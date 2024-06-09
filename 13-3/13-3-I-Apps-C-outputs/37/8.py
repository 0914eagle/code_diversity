
def max_area_of_smallest_piece(n, m, k):
    if k == 0:
        return n * m
    
    if k == 1:
        return min(n, m)
    
    if k == 2:
        return n + m - 2
    
    if k == 3:
        return n * m - 2 * min(n, m) + 2
    
    if k == 4:
        return (n - 1) * (m - 1)
    
    if k == 5:
        return n * m - 2 * min(n, m) + 4
    
    if k == 6:
        return (n - 2) * (m - 2) + 4
    
    if k == 7:
        return n * m - 2 * min(n, m) + 6
    
    if k == 8:
        return (n - 2) * (m - 2) + 6
    
    if k == 9:
        return n * m - 2 * min(n, m) + 8
    
    if k == 10:
        return (n - 2) * (m - 2) + 8
    
    if k == 11:
        return n * m - 2 * min(n, m) + 10
    
    if k == 12:
        return (n - 2) * (m - 2) + 10
    
    if k == 13:
        return n * m - 2 * min(n, m) + 12
    
    if k == 14:
        return (n - 2) * (m - 2) + 12
    
    if k == 15:
        return n * m - 2 * min(n, m) + 14
    
    if k == 16:
        return (n - 2) * (m - 2) + 14
    
    if k == 17:
        return n * m - 2 * min(n, m) + 16
    
    if k == 18:
        return (n - 2) * (m - 2) + 16
    
    if k == 19:
        return n * m - 2 * min(n, m) + 18
    
    if k == 20:
        return (n - 2) * (m - 2) + 18
    
    return -1

