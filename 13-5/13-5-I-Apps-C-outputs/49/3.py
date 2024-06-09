
def get_center_of_sphere(points):
    point1, point2, point3, point4 = points
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    x3, y3, z3 = point3
    x4, y4, z4 = point4

    # Find the equation of the plane containing the first three points
    a1 = y2 - y1
    b1 = z2 - z1
    c1 = x1 - x2
    d1 = -a1 * x1 - b1 * y1 - c1 * z1

    # Find the equation of the plane containing the second three points
    a2 = y3 - y2
    b2 = z3 - z2
    c2 = x2 - x3
    d2 = -a2 * x2 - b2 * y2 - c2 * z2

    # Find the intersection of the two planes
    denom = a1 * b2 - a2 * b1
    x = (b1 * c2 - b2 * c1) / denom
    y = (a2 * c1 - a1 * c2) / denom
    z = (a1 * b2 - a2 * b1) / denom

    # The centre of the sphere is the intersection of the two planes
    return x, y, z

