
def is_possible(rotations):
    total_angle = 0
    for angle in rotations:
        total_angle += angle
        if total_angle > 360:
            return "NO"
    return "YES"

