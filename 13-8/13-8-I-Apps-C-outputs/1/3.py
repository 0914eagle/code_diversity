
def solve(m, k, a, b):
    # Calculate the total number of sweets eaten
    total_sweets = sum(a)
    
    # Calculate the current fraction of each sweet type eaten
    current_fractions = [b[i] / total_sweets for i in range(k)]
    
    # Calculate the target fractions
    target_fractions = [a[i] / sum(a) for i in range(m)]
    
    # Calculate the maximum number of additional sweets that can be bought and eaten while keeping the diet balanced
    max_sweets = 0
    for i in range(m):
        if current_fractions[i] < target_fractions[i]:
            max_sweets += int((target_fractions[i] - current_fractions[i]) * total_sweets)
    
    return max_sweets

