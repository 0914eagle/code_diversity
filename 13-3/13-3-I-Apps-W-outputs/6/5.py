
def solve(v, a):
    # Initialize a variable to store the maximum number that can be written
    max_num = -1
    
    # Iterate through the given numbers
    for i in range(1, 10):
        # Check if the current number requires more paint than what Igor has
        if a[i] > v:
            continue
        
        # If the current number can be written, update the maximum number
        if i > max_num:
            max_num = i
    
    # Return the maximum number that can be written
    return max_num

