
def get_max_bananas(m, b):
    # Initialize the maximum number of bananas to 0
    max_bananas = 0
    
    # Loop through all possible values of x and y
    for x in range(1001):
        for y in range(10001):
            # Check if the point (x, y) is on or under the line
            if y <= (-x/m + b):
                # Add the number of bananas at this point to the maximum
                max_bananas += x + y
    
    # Return the maximum number of bananas
    return max_bananas
