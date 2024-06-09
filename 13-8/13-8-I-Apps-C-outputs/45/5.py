
def get_least_wet(T, c, d, rain):
    # Initialize variables
    wetness = 0
    speed = 0
    time = 0

    # Loop through each minute interval
    for i in range(T):
        # Calculate the amount of rain during this interval
        rain_this_interval = rain[i]

        # Calculate the amount of sweat during this interval
        sweat_this_interval = c * speed ** 2

        # Calculate the total wetness during this interval
        total_wetness = rain_this_interval + sweat_this_interval

        # Update the wetness variable
        wetness += total_wetness

        # Update the speed variable
        speed = d / T

        # Update the time variable
        time += 1

    # Return the least wetness
    return wetness

