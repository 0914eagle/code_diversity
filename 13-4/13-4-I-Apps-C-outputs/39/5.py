
def get_min_time(n, traffic_lights):
    # Initialize variables
    min_time = 0
    current_time = 0
    distance = 0

    # Iterate through each traffic light
    for i in range(n - 1):
        # Get the time, green duration, and red duration of the current light
        t, g, r = traffic_lights[i]

        # If the current time is before the start of the green duration, wait until the start of the green duration
        if current_time < t:
            current_time = t

        # If the current time is during the green duration, drive at constant speed
        if t <= current_time < t + g:
            distance += (current_time - t) * 1
            current_time = t + g

        # If the current time is during the red duration, stop driving
        if t + g <= current_time < t + g + r:
            current_time = t + g + r

        # Update the minimum time
        min_time = max(min_time, distance / 1)

    # Return the minimum time required to reach the end of the road
    return min_time

