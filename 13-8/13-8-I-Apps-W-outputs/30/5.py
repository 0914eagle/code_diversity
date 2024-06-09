
def solve(n, x):
    # Sort the list of measurements in ascending order
    x.sort()
    
    # Find the minimum and maximum values in the list
    min_val = x[0]
    max_val = x[-1]
    
    # Initialize the list of measurements for Anya
    y = []
    
    # Loop through each measurement in the list
    for i in range(n):
        # If the current measurement is the minimum value, append it to the list of measurements for Anya
        if x[i] == min_val:
            y.append(min_val)
        # If the current measurement is the maximum value, append it to the list of measurements for Anya
        elif x[i] == max_val:
            y.append(max_val)
    
    # Return the number of equal measurements and the list of measurements for Anya
    return len(y), y

