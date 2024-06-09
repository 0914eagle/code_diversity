
def get_optimal_flavor(n, ls):
    # Sort the list of flavors in ascending order
    ls.sort()
    # Initialize the sum of the flavors of the remaining apples to 0
    sum_flavors = 0
    # Iterate over the list of flavors except the last one
    for i in range(n-1):
        # Add the current flavor to the sum of the flavors of the remaining apples
        sum_flavors += ls[i]
    # Return the sum of the flavors of the remaining apples
    return sum_flavors

