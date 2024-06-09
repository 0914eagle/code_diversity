
def solve(a, b, c):
    # Find the center of the circle passing through the three points
    xc = (a[0] + b[0] + c[0]) / 3
    yc = (a[1] + b[1] + c[1]) / 3

    # Find the radius of the circle
    r = ((a[0] - xc) ** 2 + (a[1] - yc) ** 2) ** 0.5

    # Find the angle between the line connecting the center of the circle and point a, and the x-axis
    angle = (b[0] - xc, b[1] - yc)

    # Find the new position of point b after rotation
    new_b = (xc + r * cos(angle), yc + r * sin(angle))

    # Check if the new position of point b is the same as the old position of point c
    if new_b == c:
        return "Yes"
    else:
        return "No"

