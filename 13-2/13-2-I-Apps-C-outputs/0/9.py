
def get_time(x, y, v, w):
    # Calculate the distance to the target
    distance = abs(x) + abs(y)

    # Calculate the time to travel the distance at a constant speed
    time = distance / v

    # Calculate the angle of rotation needed to face the target
    angle = atan2(y, x)

    # Calculate the time to rotate to the target angle
    rotation_time = abs(angle) / w

    # Return the minimum of the time to travel the distance and the time to rotate to the target angle
    return min(time, rotation_time)

