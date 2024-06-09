
def solve(m, k, a, b):
    # Calculate the total number of sweets eaten so far
    total_sweets = sum(b)
    
    # Calculate the target fraction for each sweet type
    target_fraction = [a[i] / sum(a) for i in range(m)]
    
    # Calculate the current fraction for each sweet type
    current_fraction = [b.count(i + 1) / total_sweets for i in range(m)]
    
    # Calculate the maximum number of additional sweets that can be bought and eaten while keeping the diet balanced
    max_sweets = 0
    for i in range(m):
        if current_fraction[i] < target_fraction[i] - 1e-6:
            max_sweets += int((target_fraction[i] - current_fraction[i]) * total_sweets)
        elif current_fraction[i] > target_fraction[i] + 1e-6:
            max_sweets -= int((current_fraction[i] - target_fraction[i]) * total_sweets)
    
    return max_sweets

