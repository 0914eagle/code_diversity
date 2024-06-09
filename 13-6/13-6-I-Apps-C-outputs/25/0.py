
def can_take_all_photos(n, t, photo_times):
    # Sort the photo times in ascending order
    photo_times.sort()

    # Initialize the current time to 0
    current_time = 0

    # Loop through each photo time
    for i in range(n):
        # Check if the current time is greater than the earliest time for this photo
        if current_time < photo_times[i][0]:
            # If not, add the time it takes to take the photo
            current_time += t

        # Check if the current time is greater than the latest time for this photo
        if current_time > photo_times[i][1]:
            # If so, return "no"
            return "no"

    # If we reach this point, all photos can be taken
    return "yes"

