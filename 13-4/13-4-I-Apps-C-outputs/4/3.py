
def can_take_all_photos(n, t, photo_times):
    # Sort the photo times in ascending order
    sorted_photo_times = sorted(photo_times)

    # Initialize the current time to 0
    current_time = 0

    # Iterate through the photo times
    for i in range(n):
        # Check if the current time is before or equal to the start time of the current photo
        if current_time <= sorted_photo_times[i][0]:
            # Add the time it takes to take the photo to the current time
            current_time += t

            # Check if the current time is after or equal to the end time of the current photo
            if current_time >= sorted_photo_times[i][1]:
                # Subtract the time it takes to take the photo from the current time
                current_time -= t
        else:
            # Return no, since it is not possible to take all photos
            return "no"

    # Return yes, since it is possible to take all photos
    return "yes"

