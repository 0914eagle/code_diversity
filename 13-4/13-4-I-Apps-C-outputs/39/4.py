
def get_min_time(n, traffic_lights):
    # Initialize variables
    min_time = 0
    current_time = 0
    distance = 0

    # Iterate through each traffic light
    for i in range(n - 1):
        t, g, r = traffic_lights[i]
        current_time += t
        distance += (g + r) * 0.5
        min_time = max(min_time, distance / 1)

    # Add the time to reach the end of the road
    min_time += (n - 1) * 0.5

    return min_time

