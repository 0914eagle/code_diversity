
def get_min_breaks(k):
    # Find the smallest power of 2 greater than or equal to k
    n = 1
    while n < k:
        n *= 2
    
    # The smallest bar size is n
    bar_size = n
    
    # The number of breaks is the difference between n and k
    num_breaks = n - k
    
    return bar_size, num_breaks

