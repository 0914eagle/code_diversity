
def solve(n, x):
    # Sort the list of measurements
    x.sort()
    
    # Find the minimum and maximum values
    min_val = x[0]
    max_val = x[-1]
    
    # Initialize the list of measurements for Anya
    y = []
    
    # Loop through the measurements and find the equal measurements
    for i in range(n):
        # If the current measurement is equal to the minimum or maximum value, add it to the list of equal measurements
        if x[i] == min_val or x[i] == max_val:
            y.append(x[i])
    
    # Return the minimum number of equal measurements and the list of measurements for Anya
    return len(y), y

