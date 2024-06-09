
def solve(m, k, a, b):
    # Calculate the target fractions
    f = [ai / sum(a) for ai in a]
    
    # Initialize the number of sweets bought and eaten
    n_bought = k
    n_eaten = k
    
    # Iterate through the sequence of sweets eaten
    for i in range(k):
        # Calculate the current fraction of sweets of type b[i]
        f_current = n_eaten / n_bought
        
        # Check if the fraction is within the target range
        if f_current < f[b[i] - 1] or f_current > f[b[i] - 1] + 1:
            # If not, calculate the number of additional sweets needed
            n_additional = ceil((f[b[i] - 1] + 1) * n_bought - n_eaten)
            
            # Update the number of sweets bought and eaten
            n_bought += n_additional
            n_eaten += n_additional
    
    # Return the maximum number of additional sweets that can be bought and eaten
    return n_bought - k

