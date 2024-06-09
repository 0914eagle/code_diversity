
def solve(a):
    n = len(a)
    if n % 6 != 0:
        return n
    
    count = 0
    for i in range(0, n, 6):
        if a[i:i+6] != [4, 8, 15, 16, 23, 42]:
            count += 1
    
    return count

