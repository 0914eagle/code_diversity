
def get_min_time(n, traffic_lights):
    # Initialize variables
    min_time = 0
    current_time = 0
    distance = 0

    # Iterate through each traffic light
    for i in range(n - 1):
        t, g, r = traffic_lights[i]
        green_time = g / 3600
        red_time = r / 3600

        # If the current time is before the green time of the light, drive at constant speed
        if current_time < t:
            distance += (t - current_time)
            current_time = t

        # If the current time is during the green time of the light, drive at maximum speed
        elif current_time >= t and current_time < t + green_time:
            distance += green_time
            current_time = t + green_time

        # If the current time is during the red time of the light, stop driving
        elif current_time >= t + green_time and current_time < t + green_time + red_time:
            current_time = t + green_time + red_time

        # Update the minimum time
        min_time = max(min_time, distance / 1)

    # Return the minimum time required to reach the end of the road
    return min_time

