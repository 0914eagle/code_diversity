
def find_lipschitz_constant(f):
    # Find the maximum difference between f(x) and f(y) for any x and y
    max_diff = max([abs(f[i] - f[i-1]) for i in range(1, len(f))])
    
    # Return the maximum difference divided by the minimum distance between x and y
    return max_diff / min([abs(f[i] - f[i-1]) for i in range(1, len(f))])

