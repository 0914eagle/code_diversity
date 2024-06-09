
def find_speed(photos):
    # Initialize variables
    speed = 0
    distance = 0

    # Iterate through the photos
    for i in range(1, len(photos)):
        # Calculate the time and distance between the current and previous photo
        time_diff = photos[i][0] - photos[i-1][0]
        distance_diff = photos[i][1] - photos[i-1][1]

        # Calculate the speed between the current and previous photo
        speed_diff = distance_diff / time_diff

        # Update the maximum speed
        speed = max(speed, speed_diff)

    return speed

