
def get_max_zeroes(a, b):
    # Calculate the sum of the absolute values of a and b
    sum_abs = sum(map(abs, a)) + sum(map(abs, b))
    
    # Initialize the maximum number of zeroes to 0
    max_zeroes = 0
    
    # Iterate over all possible values of d
    for d in range(-sum_abs, sum_abs + 1):
        # Calculate the number of zeroes in the array c
        zeroes = 0
        for i in range(len(a)):
            if d * a[i] + b[i] == 0:
                zeroes += 1
        
        # Update the maximum number of zeroes if necessary
        max_zeroes = max(max_zeroes, zeroes)
    
    # Return the maximum number of zeroes
    return max_zeroes

