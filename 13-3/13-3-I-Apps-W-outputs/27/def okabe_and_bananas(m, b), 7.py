
def okabe_and_bananas(m, b):
    # Initialize the maximum number of bananas to 0
    max_bananas = 0
    
    # Loop through all possible values of x and y
    for x in range(1001):
        for y in range(10001):
            # Calculate the number of bananas in the current point
            num_bananas = x + y
            
            # Check if the point is under the line
            if y <= (-x/m + b):
                # Add the number of bananas to the maximum
                max_bananas += num_bananas
    
    # Return the maximum number of bananas
    return max_bananas

