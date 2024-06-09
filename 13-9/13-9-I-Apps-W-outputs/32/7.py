
def solve(n, k, chips):
    # Initialize the result string
    result = ""
    
    # Iterate over the given chips
    for i in range(n):
        # Get the current chip color
        current_color = chips[i]
        
        # Get the colors of the three neighboring chips
        neighbor_1 = chips[(i - 1) % n]
        neighbor_2 = chips[i]
        neighbor_3 = chips[(i + 1) % n]
        
        # Count the number of white and black chips
        num_white = neighbor_1.count("W") + neighbor_2.count("W") + neighbor_3.count("W")
        num_black = neighbor_1.count("B") + neighbor_2.count("B") + neighbor_3.count("B")
        
        # If the number of white chips is greater than the number of black chips,
        # the current chip becomes white, otherwise it becomes black
        if num_white > num_black:
            result += "W"
        else:
            result += "B"
    
    return result

