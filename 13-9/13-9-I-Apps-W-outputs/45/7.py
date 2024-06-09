
def solve(n, angles):
    total_angle = sum(angles)
    return "YES" if total_angle % 360 == 0 else "NO"

