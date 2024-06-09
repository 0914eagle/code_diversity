
def is_possible(rotations):
    total_degrees = sum(rotations)
    return total_degrees % 360 == 0

