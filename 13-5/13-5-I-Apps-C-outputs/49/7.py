
def get_center_of_sphere(points):
    point1, point2, point3, point4 = points
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    x3, y3, z3 = point3
    x4, y4, z4 = point4

    # Find the equation of the plane that passes through the first three points
    a1, b1, c1 = (y2 - y1)*(z3 - z1) - (z2 - z1)*(y3 - y1), (z2 - z1)*(x3 - x1) - (x2 - x1)*(z3 - z1), (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)
    d1 = -x1*a1 - y1*b1 - z1*c1

    # Find the equation of the plane that passes through the first three points
    a2, b2, c2 = (y4 - y1)*(z3 - z1) - (z4 - z1)*(y3 - y1), (z4 - z1)*(x3 - x1) - (x4 - x1)*(z3 - z1), (x4 - x1)*(y3 - y1) - (y4 - y1)*(x3 - x1)
    d2 = -x1*a2 - y1*b2 - z1*c2

    # Find the intersection of the two planes
    x = (b1*c2 - b2*c1)/(a1*b2 - a2*b1)
    y = (a2*c1 - a1*c2)/(a1*b2 - a2*b1)
    z = (a1*b2 - a2*b1)/(a1*b2 - a2*b1)

    return x, y, z

