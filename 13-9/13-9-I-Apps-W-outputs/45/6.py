
def is_possible(rotations):
    total_degrees = 0
    for degree in rotations:
        total_degrees += degree
        if total_degrees > 360:
            return "NO"
    return "YES"

