
def solve(a):
    n = len(a)
    if n % 6 != 0:
        return n
    
    count = 0
    i = 0
    while i < n:
        if a[i] != 4:
            count += 1
        i += 1
    
    if count == 0:
        return 0
    
    i = 0
    while i < n:
        if a[i] == 4:
            i += 1
            continue
        if a[i] == 8 and a[i+1] == 15 and a[i+2] == 16 and a[i+3] == 23 and a[i+4] == 42:
            i += 5
            continue
        count += 1
        i += 1
    
    return count

