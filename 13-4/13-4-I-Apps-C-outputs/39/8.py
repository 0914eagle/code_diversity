
def get_min_time(n, traffic_lights):
    # Initialize variables
    min_time = 0
    current_time = 0
    distance = 0

    # Loop through each traffic light
    for i in range(n - 1):
        # Get the time, green duration, and red duration of the current light
        t, g, r = traffic_lights[i]

        # If the current time is before the green duration of the light
        if current_time < g:
            # Accelerate to the green duration of the light
            distance += (g - current_time) * 1
            current_time = g

        # If the current time is during the green duration of the light
        elif current_time < g + r:
            # Maintain the current speed until the end of the green duration
            distance += (g + r - current_time) * 1
            current_time = g + r

        # If the current time is after the green duration of the light
        else:
            # Stop at the start of the red duration
            distance += (t - current_time) * 0
            current_time = t

    # Return the minimum time required to reach the end of the road
    return distance

