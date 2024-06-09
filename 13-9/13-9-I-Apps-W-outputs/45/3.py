
def is_possible_to_point_at_zero(rotations):
    total_degrees = sum(rotations)
    return total_degrees % 360 == 0

