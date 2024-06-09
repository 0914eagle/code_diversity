
def solve(T, c, d, rain):
    # Initialize variables
    wetness = 0
    speed = 0
    time = 0

    # Loop through each minute interval
    for i in range(T):
        # Calculate the amount of rain and sweat for this minute
        rain_this_min = rain[i]
        sweat_this_min = c * speed ** 2
        wetness += rain_this_min + sweat_this_min

        # If the wetness exceeds the threshold, decrease the speed
        if wetness > 50:
            speed -= 1
            wetness = 0

        # Increase the speed if possible
        if speed < 50:
            speed += 1

        # Calculate the time taken for this minute
        time += 1

    # Calculate the total distance traveled
    distance = speed * time

    # Calculate the total wetness
    wetness = rain_this_min + sweat_this_min

    # Return the total wetness
    return wetness

