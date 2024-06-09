
def find_lipschitz_constant(f):
    # Find the maximum and minimum values of the function over the given range
    max_val = max(f.values())
    min_val = min(f.values())
    
    # Calculate the Lipschitz constant as the difference between the maximum and minimum values
    # divided by the number of points in the range
    lipschitz_constant = (max_val - min_val) / len(f)
    
    return lipschitz_constant

