
def get_speed(photos):
    # Initialize the fastest speed to 0
    fastest_speed = 0

    # Iterate through the photographs
    for i in range(len(photos) - 1):
        # Get the time and distance of the current and next photograph
        current_time, current_distance = photos[i]
        next_time, next_distance = photos[i + 1]

        # Calculate the time difference and distance difference between the current and next photograph
        time_diff = next_time - current_time
        distance_diff = next_distance - current_distance

        # Calculate the speed between the current and next photograph
        speed = distance_diff / time_diff

        # Update the fastest speed if the current speed is greater than the previous fastest speed
        if speed > fastest_speed:
            fastest_speed = speed

    # Return the fastest speed
    return fastest_speed

