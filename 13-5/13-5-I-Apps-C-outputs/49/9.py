
def get_sphere_center(point1, point2, point3, point4):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    x3, y3, z3 = point3
    x4, y4, z4 = point4

    a1 = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    b1 = 2 * ((x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1) + (z2 - z1) * (z3 - z1))
    c1 = (x3 - x1) ** 2 + (y3 - y1) ** 2 + (z3 - z1) ** 2

    a2 = (x3 - x1) ** 2 + (y3 - y1) ** 2 + (z3 - z1) ** 2
    b2 = 2 * ((x3 - x1) * (x4 - x1) + (y3 - y1) * (y4 - y1) + (z3 - z1) * (z4 - z1))
    c2 = (x4 - x1) ** 2 + (y4 - y1) ** 2 + (z4 - z1) ** 2

    xc = (b1 * c2 - b2 * c1) / (a1 * c2 - a2 * c1)
    yc = (b1 * c2 - b2 * c1) / (b1 * a2 - b2 * a1)
    zc = 0

    return xc, yc, zc

