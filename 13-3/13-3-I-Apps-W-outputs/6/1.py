
def solve(v, a):
    # Initialize a variable to store the maximum number that can be written
    max_num = -1
    
    # Iterate through the given numbers
    for i in range(1, 10):
        # Check if the current number requires more paint than what Igor has
        if a[i] > v:
            continue
        
        # If the current number is not a zero, update the maximum number that can be written
        if i != 0:
            max_num = max(max_num, i)
    
    # Return the maximum number that can be written
    return max_num

