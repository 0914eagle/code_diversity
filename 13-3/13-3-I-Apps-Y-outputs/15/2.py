
def get_min_diff(s):
    # Initialize the minimum difference and the current difference
    min_diff = float('inf')
    curr_diff = 0
    
    # Loop through all possible starting indices for the three consecutive digits
    for i in range(len(s) - 2):
        # Extract the three consecutive digits and convert them to an integer
        x = int(s[i:i+3])
        
        # Calculate the absolute difference between x and 753
        curr_diff = abs(x - 753)
        
        # Update the minimum difference if necessary
        if curr_diff < min_diff:
            min_diff = curr_diff
    
    # Return the minimum difference
    return min_diff

