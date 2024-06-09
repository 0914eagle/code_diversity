
def solve(n, x):
    # Sort the list of measurements in ascending order
    x.sort()
    
    # Initialize the minimum number of equal measurements to 0
    min_equal = 0
    
    # Initialize the list of measurements to write in Anya's work
    y = []
    
    # Loop through each measurement in Kirill's work
    for i in range(n):
        # Check if the current measurement is equal to the previous measurement
        if i > 0 and x[i] == x[i-1]:
            # Increment the minimum number of equal measurements
            min_equal += 1
        # Otherwise, append the current measurement to the list of measurements to write in Anya's work
        else:
            y.append(x[i])
    
    # Return the minimum number of equal measurements and the list of measurements to write in Anya's work
    return min_equal, y

