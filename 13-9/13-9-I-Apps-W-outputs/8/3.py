
def get_max_messiness(n, k):
    if n == 1:
        return 0
    
    max_messiness = 0
    for i in range(1, n):
        for j in range(i+1, n):
            max_messiness += min(k, n-i+j)
    
    return max_messiness

