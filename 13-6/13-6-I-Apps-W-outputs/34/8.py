
def get_min_time(a, b, x, y):
    # Initialize a dictionary to store the minimum time to reach each floor
    # from the a-th floor of A
    min_time = {a: 0}

    # Loop through each floor from a to b
    for i in range(a, b + 1):
        # If we have already calculated the minimum time to reach this floor,
        # skip this iteration
        if i in min_time:
            continue

        # If we are on the b-th floor, return the minimum time to reach this floor
        if i == b:
            return min_time[i]

        # Get the minimum time to reach the next floor from the current floor
        next_floor_time = min(min_time[i - 1] + x, min_time[i + 1] + x)

        # If we are not on the first or last floor,
        # consider taking the stairs to the adjacent floor
        if i > 1 and i < 100:
            next_floor_time = min(next_floor_time, min_time[i - 2] + y + y)

        # Update the minimum time to reach the current floor
        min_time[i] = next_floor_time

    # If we reach this point, it means that we could not find a path to the b-th floor,
    # so return -1
    return -1

