
def get_speed(photos):
    # Initialize variables
    speed = 0
    time = 0
    distance = 0

    # Loop through the photos
    for photo in photos:
        # Calculate the time and distance between the current and previous photo
        current_time = photo[0]
        current_distance = photo[1]
        time_diff = current_time - time
        distance_diff = current_distance - distance

        # Calculate the speed using the time and distance differences
        speed = distance_diff / time_diff

        # Update the time and distance for the next iteration
        time = current_time
        distance = current_distance

    # Return the greatest integral speed
    return int(speed)

