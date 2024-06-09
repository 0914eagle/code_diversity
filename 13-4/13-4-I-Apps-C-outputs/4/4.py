
def can_take_all_photos(n, t, times):
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

        # Check if the current time is greater than the end time of the photo
        if current_time > sorted_times[i][1]:
            # Return no, it is not possible to take all photos
            return "no"

    # Return yes, it is possible to take all photos
    return "yes"

