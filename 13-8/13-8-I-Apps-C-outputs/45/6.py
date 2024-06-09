
def solve(T, c, d, rain):
    # Calculate the maximum speed at which you can cycle to be home by T minutes
    max_speed = d / (T * 60)

    # Initialize the minimum wetness level
    min_wetness = 0

    # Iterate through each minute interval
    for i in range(T):
        # Calculate the wetness level from rain during this interval
        rain_interval = rain[i]

        # Calculate the wetness level from sweating during this interval
        sweat_interval = c * max_speed ** 2 * (i + 1)

        # Update the minimum wetness level
        min_wetness += max(rain_interval, sweat_interval)

    return min_wetness

