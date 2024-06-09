
def solve(n, x):
    # Sort the measurements of Kirill in ascending order
    x.sort()
    
    # Find the minimum and maximum values among Kirill's measurements
    min_value = x[0]
    max_value = x[n-1]
    
    # Initialize the number of equal measurements to 0
    equal_measurements = 0
    
    # Iterate through the measurements of Kirill
    for i in range(n):
        # If the current measurement is equal to the minimum value among Kirill's measurements
        if x[i] == min_value:
            # Increment the number of equal measurements
            equal_measurements += 1
    
    # Initialize the list of measurements for Anya
    y = []
    
    # If the number of equal measurements is even
    if equal_measurements % 2 == 0:
        # Iterate through the measurements of Kirill
        for i in range(n):
            # If the current measurement is equal to the minimum value among Kirill's measurements
            if x[i] == min_value:
                # Add the current measurement to the list of measurements for Anya
                y.append(x[i])
    
    # If the number of equal measurements is odd
    else:
        # Iterate through the measurements of Kirill
        for i in range(n):
            # If the current measurement is equal to the minimum value among Kirill's measurements
            if x[i] == min_value:
                # Add the current measurement to the list of measurements for Anya
                y.append(x[i])
                # Break the loop
                break
    
    # Return the number of equal measurements and the list of measurements for Anya
    return equal_measurements, y

