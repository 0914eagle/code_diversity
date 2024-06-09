
def solve(n, x, v):
    # Sort the friends by their current position
    sorted_x = sorted(x)

    # Initialize the minimum time needed to gather all the friends
    min_time = 0

    # Iterate over the friends and calculate the time needed to gather them
    for i in range(n - 1):
        # Calculate the distance between the current friend and the previous friend
        distance = sorted_x[i + 1] - sorted_x[i]

        # Calculate the time needed to cover the distance at the maximum speed
        time = distance / v[i]

        # Add the time to the minimum time needed to gather all the friends
        min_time += time

    return min_time

