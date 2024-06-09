
def get_min_time(n, x, v):
    # Sort the friends by their current coordinates
    sorted_x = sorted(x)

    # Initialize the minimum time needed to gather all the friends
    min_time = 0

    # Loop through each friend and calculate their travel time
    for i in range(n):
        # Calculate the distance between the current friend and the next friend
        distance = sorted_x[i + 1] - sorted_x[i]

        # Calculate the travel time for the current friend
        travel_time = distance / v[i]

        # Add the travel time to the minimum time needed
        min_time += travel_time

    return min_time

