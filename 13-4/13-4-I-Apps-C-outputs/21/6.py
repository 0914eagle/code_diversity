
def get_time_to_reach_destination(x1, y1, x2, y2, v_max, t, wind_speeds):
    # Calculate the distance between the two points
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Initialize the time and velocity variables
    time = 0
    velocity = 0

    # Loop through the wind speeds
    for i in range(t):
        # Calculate the new velocity and time
        velocity += wind_speeds[i][0]
        time += velocity / v_max

        # Calculate the new position
        x1 += velocity * wind_speeds[i][0] / v_max
        y1 += velocity * wind_speeds[i][1] / v_max

    # Calculate the time to reach the destination at the maximum speed
    time_max_speed = distance / v_max

    # Return the minimum time
    return min(time, time_max_speed)

