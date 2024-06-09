
def get_min_time(n, traffic_lights):
    # Initialize variables
    min_time = 0
    current_time = 0
    speed = 1
    distance = 0

    # Iterate through each traffic light
    for i in range(n - 1):
        # Get the time, green duration, and red duration of the current light
        t, g, r = traffic_lights[i]

        # If the current time is before the start of the green duration, accelerate
        if current_time < t:
            distance += (t - current_time) * speed
            current_time = t

        # If the current time is during the green duration, maintain speed
        elif current_time < t + g:
            distance += speed
            current_time += 1

        # If the current time is during the red duration, stop
        elif current_time < t + g + r:
            current_time += 1

        # Update the minimum time
        min_time = max(min_time, distance / speed)

    # Return the minimum time required to reach the end of the road
    return min_time

