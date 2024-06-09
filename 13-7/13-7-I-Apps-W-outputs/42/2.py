
def get_min_time(n, x, v):
    # Sort the points by their x-coordinate
    sorted_x = sorted(x)

    # Initialize the minimum time to gather all friends to infinity
    min_time = float('inf')

    # Loop through each point and find the minimum time to gather all friends at that point
    for i in range(n):
        # Calculate the time it takes for each friend to reach the current point
        time = [abs(x[i] - sorted_x[j]) / v[j] for j in range(n)]

        # Calculate the minimum time it takes for all friends to reach the current point
        min_time = min(min_time, max(time))

    return min_time

