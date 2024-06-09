
def get_max_zeroes(a, b):
    # Calculate the sum of the absolute values of a and b
    sum_abs = sum(map(abs, a)) + sum(map(abs, b))
    
    # Calculate the number of zeroes in the result array
    num_zeroes = sum_abs - len(a)
    
    return num_zeroes

