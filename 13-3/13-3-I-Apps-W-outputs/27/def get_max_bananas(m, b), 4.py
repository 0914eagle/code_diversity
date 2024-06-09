
def get_max_bananas(m, b):
    # Initialize the maximum number of bananas to 0
    max_bananas = 0
    
    # Loop through all possible values of x and y
    for x in range(1001):
        for y in range(10001):
            # Check if the point (x, y) is on or under the line
            if y <= (-x/m + b):
                # Calculate the number of bananas at this point
                num_bananas = x + y
                # Update the maximum number of bananas if necessary
                max_bananas = max(max_bananas, num_bananas)
    
    # Return the maximum number of bananas
    return max_bananas

