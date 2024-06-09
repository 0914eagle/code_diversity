
def check_rotations(rotations):
    total_degrees = sum(rotations)
    return total_degrees % 360 == 0

