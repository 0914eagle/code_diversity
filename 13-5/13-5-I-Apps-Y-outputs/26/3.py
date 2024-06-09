
def get_max_zeroes(a, b):
    # Calculate the sum of the absolute values of a and b
    sum_abs = sum(map(abs, a)) + sum(map(abs, b))
    
    # Initialize the maximum number of zeroes to 0
    max_zeroes = 0
    
    # Iterate over all possible values of d
    for d in range(-sum_abs, sum_abs + 1):
        # Initialize the number of zeroes to 0
        zeroes = 0
        
        # Iterate over all elements of a and b
        for i in range(len(a)):
            # Calculate the value of c_i
            c_i = d * a[i] + b[i]
            
            # Check if c_i is zero
            if c_i == 0:
                # Increment the number of zeroes
                zeroes += 1
        
        # Check if the number of zeroes is greater than the maximum number of zeroes
        if zeroes > max_zeroes:
            # Update the maximum number of zeroes
            max_zeroes = zeroes
    
    # Return the maximum number of zeroes
    return max_zeroes

