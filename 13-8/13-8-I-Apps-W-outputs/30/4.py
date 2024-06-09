
def solve(n, x):
    # Sort the input array
    x.sort()
    
    # Find the minimum and maximum values
    min_val = x[0]
    max_val = x[-1]
    
    # Initialize the output array
    y = [0] * n
    
    # Fill the output array with the minimum value
    for i in range(n):
        y[i] = min_val
    
    # Return the minimum possible number of equal measurements
    return n - (max_val - min_val)

