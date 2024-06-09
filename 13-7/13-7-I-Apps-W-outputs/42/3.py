
def solve(n, x, v):
    # Sort the friends by their current position
    sorted_x = sorted(x)

    # Initialize the minimum time to gather all friends as 0
    min_time = 0

    # Loop through each friend and add their time to the minimum time
    for i in range(n):
        # Calculate the distance between the current friend and the previous friend
        distance = abs(sorted_x[i] - sorted_x[i - 1])

        # Calculate the time it takes for the friend to cover the distance
        time = distance / v[i]

        # Add the time to the minimum time
        min_time += time

    # Return the minimum time
    return min_time

