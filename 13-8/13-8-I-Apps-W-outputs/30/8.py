
def solve(n, x):
    # Sort the measurements in ascending order
    x.sort()
    
    # Find the minimum and maximum values
    min_value = x[0]
    max_value = x[-1]
    
    # Initialize the number of equal measurements to 0
    num_equal = 0
    
    # Iterate over the measurements
    for i in range(n):
        # If the current measurement is equal to the minimum or maximum value, increment the number of equal measurements
        if x[i] == min_value or x[i] == max_value:
            num_equal += 1
    
    # Return the minimum possible number of equal measurements and the values Anya should write
    return num_equal, [min_value] * num_equal

