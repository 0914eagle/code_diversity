
def solve(m, k, a, b):
    # Calculate the total number of sweets eaten
    total_sweets = sum(a)
    
    # Calculate the current fraction of each sweet type
    current_fractions = [b[i] / total_sweets for i in range(k)]
    
    # Calculate the target fraction of each sweet type
    target_fractions = [a[i] / sum(a) for i in range(m)]
    
    # Calculate the maximum number of additional sweets that can be bought
    max_sweets = total_sweets * (1 - min(current_fractions)) // min(target_fractions)
    
    return max_sweets

