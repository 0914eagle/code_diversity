
def find_lipschitz_constant(f):
    # Find the maximum difference between f(x) and f(y) for any x and y
    max_diff = max([abs(f(x) - f(y)) for x in f for y in f])
    
    # Return the maximum difference divided by the minimum distance between x and y
    return max_diff / min([abs(x - y) for x in f for y in f])

