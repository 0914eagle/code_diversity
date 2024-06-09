
def rotate_lock(rotations, angles):
    total_angle = sum(angles)
    if total_angle == 360:
        return "YES"
    else:
        return "NO"

