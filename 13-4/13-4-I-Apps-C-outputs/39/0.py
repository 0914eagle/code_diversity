
def get_min_time(n, traffic_lights):
    # Initialize variables
    min_time = 0
    current_time = 0
    distance = 0

    # Loop through each traffic light
    for i in range(n - 1):
        # Get the time, green duration, and red duration of the current light
        t, g, r = traffic_lights[i]

        # If the current time is before the time the light switches to green, wait until then
        if current_time < t:
            current_time = t

        # Accelerate for the green duration
        current_time += g
        distance += g

        # If the current time is before the time the light switches to red, wait until then
        if current_time < t + r:
            current_time = t + r

        # Deaccelerate for the red duration
        current_time += r
        distance += r

    # Return the minimum time required to reach the end of the road
    return distance / 1

