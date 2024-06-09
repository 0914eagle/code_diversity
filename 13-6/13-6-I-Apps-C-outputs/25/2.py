
def can_take_all_photos(n, t, times):
    # Sort the times in ascending order
    sorted_times = sorted(times)

    # Initialize the current time to 0
    current_time = 0

    # Iterate through the times and check if they can be taken within the given time frame
    for i in range(n):
        start_time, end_time = sorted_times[i]
        if current_time + t <= start_time:
            current_time = start_time + t
        elif current_time + t > end_time:
            return "no"
        else:
            current_time += t

    return "yes"

