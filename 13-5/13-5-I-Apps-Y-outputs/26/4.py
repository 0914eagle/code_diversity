
def get_max_zeroes(a, b):
    # Find the maximum and minimum values in both arrays
    max_a = max(a)
    max_b = max(b)
    min_a = min(a)
    min_b = min(b)
    
    # Calculate the range of possible values for d
    range_d = max_a - min_a + max_b - min_b
    
    # Initialize the maximum number of zeroes to 0
    max_zeroes = 0
    
    # Iterate over all possible values of d
    for d in range(range_d + 1):
        # Calculate the number of zeroes in the current array c
        zeroes = 0
        for i in range(len(a)):
            if (d * a[i] + b[i]) == 0:
                zeroes += 1
        
        # Update the maximum number of zeroes if necessary
        if zeroes > max_zeroes:
            max_zeroes = zeroes
    
    return max_zeroes

