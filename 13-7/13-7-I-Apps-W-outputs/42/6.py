
def get_min_time(n, x, v):
    # Sort the points by their x coordinates
    sorted_x = sorted(x)

    # Initialize the minimum time to 0
    min_time = 0

    # Loop through the points and calculate the time needed for each friend to reach the next point
    for i in range(n - 1):
        # Calculate the distance between the current point and the next point
        dist = sorted_x[i + 1] - sorted_x[i]

        # Calculate the time needed for the friend to cover the distance at their maximum speed
        time = dist / v[i]

        # Add the time to the minimum time
        min_time += time

    # Return the minimum time
    return min_time

