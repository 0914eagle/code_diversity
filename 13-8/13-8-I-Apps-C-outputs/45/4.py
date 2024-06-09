
def get_least_wet(T, c, d, rain):
    # Initialize variables
    sweat = 0
    rain_so_far = 0
    time_left = T
    current_speed = 0
    optimal_speed = 0

    # Loop through each minute interval
    for i in range(len(rain)):
        # Calculate the amount of rain and sweat for this interval
        rain_this_interval = rain[i]
        sweat_this_interval = c * current_speed ** 2
        total_wetness = rain_this_interval + sweat_this_interval

        # Check if the current speed is optimal for this interval
        if total_wetness > time_left * d:
            optimal_speed = current_speed
            break

        # Update the variables for the next interval
        sweat += sweat_this_interval
        rain_so_far += rain_this_interval
        time_left -= 1
        current_speed += 1

    # Calculate the total wetness
    total_wetness = sweat + rain_so_far

    # Return the least wetness
    return total_wetness

