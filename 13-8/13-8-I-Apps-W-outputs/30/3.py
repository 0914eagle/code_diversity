
def get_equal_measurements(x):
    # Sort the list of measurements
    x.sort()
    # Initialize the minimum number of equal measurements to 0
    min_equal = 0
    # Initialize the list of equal measurements to be empty
    equal = []
    # Iterate over the measurements
    for i in range(len(x)):
        # Check if the current measurement is equal to the previous measurement
        if i > 0 and x[i] == x[i-1]:
            # If it is, add it to the list of equal measurements
            equal.append(x[i])
        # If the current measurement is not equal to the previous measurement, check if it is equal to the next measurement
        elif i < len(x)-1 and x[i] == x[i+1]:
            # If it is, add it to the list of equal measurements
            equal.append(x[i])
        # If the current measurement is not equal to the previous or next measurement, check if it is equal to the minimum measurement
        elif x[i] == x[0]:
            # If it is, add it to the list of equal measurements
            equal.append(x[i])
        # If the current measurement is not equal to the previous, next, or minimum measurement, check if it is equal to the maximum measurement
        elif x[i] == x[-1]:
            # If it is, add it to the list of equal measurements
            equal.append(x[i])
    # Return the minimum number of equal measurements and the list of equal measurements
    return (min_equal, equal)

