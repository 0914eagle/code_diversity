
def get_min_diff(s):
    # Initialize the minimum difference and the current difference
    min_diff = float('inf')
    curr_diff = 0
    
    # Iterate over the length of the string
    for i in range(len(s) - 2):
        # Get the current substring of length 3
        substring = s[i:i+3]
        
        # Convert the substring to an integer
        x = int(substring)
        
        # Calculate the difference between x and 753
        curr_diff = abs(x - 753)
        
        # Update the minimum difference if necessary
        if curr_diff < min_diff:
            min_diff = curr_diff
    
    # Return the minimum difference
    return min_diff

