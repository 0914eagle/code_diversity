
def get_max_zeroes(a, b):
    # Find the maximum and minimum values in both arrays
    max_a = max(a)
    max_b = max(b)
    min_a = min(a)
    min_b = min(b)
    
    # Calculate the range of possible values for d
    d_range = [max_a * min_b, min_a * max_b]
    
    # Initialize the maximum number of zeroes to 0
    max_zeroes = 0
    
    # Iterate over the range of possible values for d
    for d in range(d_range[0], d_range[1] + 1):
        # Calculate the number of zeroes in the current array
        zeroes = 0
        for i in range(len(a)):
            if d * a[i] + b[i] == 0:
                zeroes += 1
        
        # Update the maximum number of zeroes if necessary
        if zeroes > max_zeroes:
            max_zeroes = zeroes
    
    return max_zeroes

