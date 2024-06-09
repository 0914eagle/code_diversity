
def get_min_time(a, b, x, y):
    # Initialize a dictionary to store the minimum time to reach each floor
    # from the a-th floor of A
    min_time = {a: 0}

    # Loop through each floor from a to b
    for i in range(a, b + 1):
        # If we have already calculated the minimum time to reach this floor,
        # skip this floor
        if i in min_time:
            continue

        # Initialize the minimum time to reach this floor as infinity
        min_time[i] = float("inf")

        # Loop through each floor from a to i
        for j in range(a, i + 1):
            # If we can reach the j-th floor from the a-th floor in t minutes,
            # and the j-th floor is connected to the i-th floor in x minutes,
            # then we can reach the i-th floor from the a-th floor in t + x minutes
            if j in min_time and min_time[j] + x <= min_time[i]:
                min_time[i] = min_time[j] + x

        # If we can reach the i-th floor from the a-th floor in t minutes,
        # and the i-th floor is connected to the (i+1)-th floor in y minutes,
        # then we can reach the (i+1)-th floor from the a-th floor in t + y minutes
        if i in min_time and min_time[i] + y <= min_time[i + 1]:
            min_time[i + 1] = min_time[i] + y

    # Return the minimum time to reach the b-th floor of B from the a-th floor of A
    return min_time[b]

