
def find_lipschitz_constant(f):
    # Find the maximum difference between f(x) and f(y) for any x and y
    max_diff = max([abs(f[i] - f[i-1]) for i in range(1, len(f))])
    # Return the maximum difference divided by the difference between x and y
    return max_diff / (f[-1][0] - f[0][0])

