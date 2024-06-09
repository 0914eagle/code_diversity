
def is_possible(n, t, times):
    # Sort the times in ascending order
    times.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through the times and check if they can be taken within the given time frame
    for i in range(n):
        start_time, end_time = times[i]
        if current_time + t <= start_time:
            current_time = start_time + t
        elif current_time + t > start_time and current_time + t <= end_time:
            current_time = end_time
        else:
            return "no"

    # If all the times can be taken, return "yes"
    return "yes"

