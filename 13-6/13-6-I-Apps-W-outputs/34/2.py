
def get_min_time(a, b, x, y):
    # Initialize a dictionary to store the minimum time to reach each floor
    # from the a-th floor of A
    min_time = {a: 0}

    # Loop until we reach the b-th floor of B
    while b not in min_time:
        # Get the minimum time to reach the next floor from the current floor
        next_floor = min((f for f in range(a, b + 1) if f not in min_time), key=lambda f: min_time[f])
        min_time[next_floor] = min(min_time[next_floor], min_time[a] + x if next_floor > a else min_time[a])
        a = next_floor

    return min_time[b]

