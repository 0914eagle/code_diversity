
def solve(n, rotations):
    total_angle = sum(rotations)
    return "YES" if total_angle % 360 == 0 else "NO"

