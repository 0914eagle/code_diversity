
def get_min_time(a, b, x, y):
    # Initialize a dictionary to store the minimum time to reach each floor
    # from the a-th floor of A
    min_time = {a: 0}

    # Loop through each floor from a to b
    for floor in range(a, b + 1):
        # If the floor is already in the dictionary, skip it
        if floor in min_time:
            continue

        # If the floor is the a-th floor of A, the minimum time to reach it is 0
        if floor == a:
            min_time[floor] = 0
            continue

        # If the floor is the b-th floor of B, the minimum time to reach it is the time to reach the (b-1)-th floor of B
        if floor == b:
            min_time[floor] = min_time[b - 1]
            continue

        # If the floor is not the a-th or b-th floor of A or B, find the minimum time to reach it
        min_time[floor] = min(min_time[floor - 1] + x, min_time[floor - x] + y)

    return min_time[b]

