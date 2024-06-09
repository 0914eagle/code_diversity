
def get_time(x, y, v, w):
    # Calculate the distance to the target location
    distance = abs(x) + abs(y)

    # Calculate the time to travel the distance at the given speed
    time = distance / v

    # Calculate the angle of rotation needed to face the target location
    angle = atan2(y, x)

    # Calculate the time to rotate to the target angle at the given rate
    rotation_time = abs(angle) / w

    # Return the total time needed to get to the target location
    return time + rotation_time

