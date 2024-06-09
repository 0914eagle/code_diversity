
def get_max_zeroes(a, b):
    # Calculate the sum of the absolute values of a and b
    sum_abs = sum(map(abs, a + b))
    
    # Initialize the maximum number of zeroes to 0
    max_zeroes = 0
    
    # Iterate over all possible values of d
    for d in range(-sum_abs, sum_abs + 1):
        # Calculate the number of zeroes in the current array c
        zeroes = sum(1 for x in (d * x + y for x, y in zip(a, b)) if x == 0)
        
        # Update the maximum number of zeroes if necessary
        max_zeroes = max(max_zeroes, zeroes)
    
    return max_zeroes

