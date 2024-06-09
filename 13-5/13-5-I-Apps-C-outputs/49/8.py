
def get_center(points):
    point1, point2, point3, point4 = points
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    x3, y3, z3 = point3
    x4, y4, z4 = point4

    # Find the equation of the plane that passes through point1, point2 and point3
    a1, b1, c1 = point1
    a2, b2, c2 = point2
    a3, b3, c3 = point3

    d1 = a1 * b2 + b1 * c2 + c1 * a2
    d2 = a2 * b3 + b2 * c3 + c2 * a3
    d3 = a3 * b1 + b3 * c1 + c3 * a1

    # Find the equation of the plane that passes through point1, point2 and point4
    a1, b1, c1 = point1
    a4, b4, c4 = point4

    d4 = a1 * b4 + b1 * c4 + c1 * a4
    d5 = a4 * b1 + b4 * c1 + c4 * a1

    # Find the intersection of the two planes
    x = (d1 * c2 - c1 * d2) / (b1 * c2 - b2 * c1)
    y = (a1 * d2 - a2 * d1) / (a1 * b2 - a2 * b1)
    z = (d3 * b1 - b3 * d1) / (b3 * c1 - b1 * c3)

    return x, y, z

