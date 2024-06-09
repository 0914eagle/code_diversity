
def solve(n, x):
    # Sort the measurements in ascending order
    x.sort()
    
    # Find the minimum and maximum values
    min_val = x[0]
    max_val = x[n-1]
    
    # Initialize the number of equal measurements to 0
    equal_measurements = 0
    
    # Loop through the measurements
    for i in range(n):
        # Check if the current measurement is equal to the minimum or maximum value
        if x[i] == min_val or x[i] == max_val:
            # Increment the number of equal measurements
            equal_measurements += 1
    
    # Return the minimum possible number of equal measurements and the corresponding values
    return equal_measurements, [min_val] * equal_measurements + [max_val] * (n - equal_measurements)

