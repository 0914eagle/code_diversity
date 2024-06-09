
def get_speed(photographs):
    # Initialize variables
    max_speed = 0
    time_intervals = []

    # Iterate through the photographs
    for i in range(len(photographs)):
        # Calculate the time interval between the current photograph and the previous photograph
        if i > 0:
            time_interval = photographs[i][0] - photographs[i-1][0]
            time_intervals.append(time_interval)

        # Calculate the distance traveled between the current photograph and the previous photograph
        if i > 0 and photographs[i][1] > photographs[i-1][1]:
            distance_traveled = photographs[i][1] - photographs[i-1][1]
        else:
            distance_traveled = 0

        # Calculate the speed based on the time interval and distance traveled
        speed = distance_traveled / time_interval

        # Update the maximum speed if the current speed is greater than the maximum speed
        if speed > max_speed:
            max_speed = speed

    return max_speed

