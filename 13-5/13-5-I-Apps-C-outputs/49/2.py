
import math

def get_center(points):
    point1, point2, point3, point4 = points
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    x3, y3, z3 = point3
    x4, y4, z4 = point4

    # Calculate the distances between the points and the origin
    d1 = math.sqrt(x1**2 + y1**2 + z1**2)
    d2 = math.sqrt(x2**2 + y2**2 + z2**2)
    d3 = math.sqrt(x3**2 + y3**2 + z3**2)
    d4 = math.sqrt(x4**2 + y4**2 + z4**2)

    # Calculate the dot products of the points and the origin
    dot1 = x1*x2 + y1*y2 + z1*z2
    dot2 = x2*x3 + y2*y3 + z2*z3
    dot3 = x3*x4 + y3*y4 + z3*z4
    dot4 = x4*x1 + y4*y1 + z4*z1

    # Calculate the denominator of the formula
    denom = d1*d2*d3*d4 + dot1*dot2*dot3*dot4

    # Calculate the x coordinate of the center
    x_center = (dot1*dot2 + dot2*dot3 + dot3*dot4 + dot4*dot1)/denom

    # Calculate the y coordinate of the center
    y_center = (dot1*dot3 + dot2*dot4 + dot3*dot1 + dot4*dot2)/denom

    # Calculate the z coordinate of the center
    z_center = (dot1*dot4 + dot2*dot1 + dot3*dot2 + dot4*dot3)/denom

    return x_center, y_center, z_center

