
def can_take_photos(n, t, times):
    # Sort the times in ascending order
    sorted_times = sorted(times)

    # Initialize the current time to 0
    current_time = 0

    # Loop through each time period
    for i in range(n):
        # Check if the current time is within the time period
        if current_time < sorted_times[i][0]:
            # Add the time it takes to take the photo to the current time
            current_time += t
        else:
            # The current time is within the time period, so check if the photo can be taken
            if current_time + t <= sorted_times[i][1]:
                # The photo can be taken, so add the time it takes to take the photo to the current time
                current_time += t
            else:
                # The photo cannot be taken, so return "no"
                return "no"

    # If all photos can be taken, return "yes"
    return "yes"

