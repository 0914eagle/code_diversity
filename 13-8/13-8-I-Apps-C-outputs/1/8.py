
def solve(m, k, a, b):
    # Calculate the total number of sweets eaten
    total = sum(b)
    
    # Calculate the minimum and maximum number of sweets that can be eaten to maintain balance
    min_sweets = total // m
    max_sweets = total // m + 1
    
    # Initialize the number of additional sweets that can be eaten
    additional_sweets = 0
    
    # Loop through each type of sweet and calculate the minimum and maximum number of sweets that can be eaten of that type to maintain balance
    for i in range(m):
        min_i = min_sweets * a[i] // sum(a)
        max_i = max_sweets * a[i] // sum(a)
        
        # Check if the current type of sweet can be eaten an additional sweet
        if b[i] < min_i:
            additional_sweets += min_i - b[i]
        elif b[i] > max_i:
            additional_sweets += max_i - b[i]
    
    # Return the maximum number of additional sweets that can be eaten
    return additional_sweets

