
def find_lipschitz_constant(f):
    # Find the maximum and minimum values of the function over the input domain
    max_val = max(f.values())
    min_val = min(f.values())
    
    # Calculate the Lipschitz constant as the difference between the maximum and minimum values divided by the number of input points minus 1
    lipschitz_constant = (max_val - min_val) / (len(f) - 1)
    
    return lipschitz_constant

