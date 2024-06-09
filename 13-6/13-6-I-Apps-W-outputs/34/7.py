
def find_min_time(a, b, x, y):
    # Initialize a dictionary to store the minimum time to reach each floor
    # from the a-th floor of A
    min_time = {a: 0}

    # Loop through each floor from a to b
    for i in range(a, b + 1):
        # If the current floor is not in the dictionary, add it
        if i not in min_time:
            min_time[i] = float("inf")

        # Loop through each floor that is connected to the current floor
        for j in range(i - 1, -1, -1):
            # If the floor is in the dictionary and the time to reach it
            # from the a-th floor of A is less than the current minimum time,
            # update the minimum time
            if j in min_time and min_time[j] + x < min_time[i]:
                min_time[i] = min_time[j] + x

        # If the current floor is not the b-th floor of B,
        # add the time to reach the next floor by taking the stairs
        if i != b:
            min_time[i] += y

    # Return the minimum time to reach the b-th floor of B from the a-th floor of A
    return min_time[b]

