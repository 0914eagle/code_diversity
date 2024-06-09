
def get_min_breaks_and_bar_size(k):
    # Find the smallest power of 2 greater than or equal to k
    bar_size = 1
    while bar_size < k:
        bar_size *= 2
    
    # Calculate the number of breaks needed to get k squares
    num_breaks = 0
    while bar_size > k:
        bar_size //= 2
        num_breaks += 1
    
    return bar_size, num_breaks

