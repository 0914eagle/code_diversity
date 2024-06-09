
def get_min_time(n, traffic_lights):
    # Initialize variables
    min_time = 0
    current_time = 0
    distance = 0

    # Loop through each traffic light
    for i in range(n - 1):
        # Get the time, green duration, and red duration of the current light
        t, g, r = traffic_lights[i]

        # If the current time is before the start of the green duration, wait until the start of the green duration
        if current_time < t:
            current_time = t

        # If the current time is during the green duration, drive at a constant rate of 1 m/s^2
        if t <= current_time < t + g:
            distance += 1
            current_time += 1

        # If the current time is during the red duration, stop at the current location
        if t + g <= current_time < t + g + r:
            current_time = t + g + r

        # Update the minimum time required to reach the end of the road
        min_time = max(min_time, current_time)

    # Return the minimum time required to reach the end of the road
    return min_time

