
def solve(n, measurements):
    # Sort the measurements in ascending order
    measurements.sort()
    
    # Initialize the minimum number of equal measurements to 0
    min_equal_measurements = 0
    
    # Initialize the list of equal measurements to be an empty list
    equal_measurements = []
    
    # Loop through each measurement
    for i in range(n):
        # Check if the current measurement is equal to the previous measurement
        if i > 0 and measurements[i] == measurements[i-1]:
            # If it is equal, add it to the list of equal measurements
            equal_measurements.append(measurements[i])
        # If the current measurement is not equal to the previous measurement, check if it is equal to the next measurement
        elif i < n-1 and measurements[i] == measurements[i+1]:
            # If it is equal, add it to the list of equal measurements
            equal_measurements.append(measurements[i])
    
    # Get the minimum number of equal measurements by returning the length of the list of equal measurements
    min_equal_measurements = len(equal_measurements)
    
    # Return the minimum number of equal measurements and the list of equal measurements
    return min_equal_measurements, equal_measurements

