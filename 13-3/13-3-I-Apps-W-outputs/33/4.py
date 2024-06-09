
def get_arrow_points(px, py, vx, vy, a, b, c, d):
    # Calculate the coordinates of the arrow points
    x1 = px + vx
    y1 = py + vy
    x2 = x1 + a
    y2 = y1
    x3 = x2 + c
    y3 = y2 + d
    x4 = x3 + c
    y4 = y3 - d
    x5 = x4 - a
    y5 = y4
    x6 = x5 - a
    y6 = y5 - b
    x7 = x6
    y7 = y6 - b
    x8 = x7 + vx
    y8 = y7 + vy

    # Return the coordinates of the arrow points in counter-clockwise order
    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8)]

