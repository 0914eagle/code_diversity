
import math

def get_center(points):
    point1, point2, point3, point4 = points
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    x3, y3, z3 = point3
    x4, y4, z4 = point4

    # Calculate the distance between the points
    d12 = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    d13 = math.sqrt((x1-x3)**2 + (y1-y3)**2 + (z1-z3)**2)
    d14 = math.sqrt((x1-x4)**2 + (y1-y4)**2 + (z1-z4)**2)
    d23 = math.sqrt((x2-x3)**2 + (y2-y3)**2 + (z2-z3)**2)
    d24 = math.sqrt((x2-x4)**2 + (y2-y4)**2 + (z2-z4)**2)
    d34 = math.sqrt((x3-x4)**2 + (y3-y4)**2 + (z3-z4)**2)

    # Calculate the coordinates of the center of the sphere
    xc = (d12*d13*d14*(y2-y3)*(y2-y4)*(y3-y4) + d23*d24*d34*(y1-y3)*(y1-y4)*(y3-y4) + d12*d23*d34*(y1-y2)*(y1-y4)*(y2-y4)) / (2*(d12*d23 - d13*d24 + d14*d23 - d13*d14 - d12*d24 + d14*d22))
    yc = (d12*d13*d14*(z2-z3)*(z2-z4)*(z3-z4) + d23*d24*d34*(z1-z3)*(z1-z4)*(z3-z4) + d12*d23*d34*(z1-z2)*(z1-z4)*(z2-z4)) / (2*(d12*d23 - d13*d24 + d14*d23 - d13*d14 - d12*d24 + d14*d22))
    zc = (d12*d13*d14*(x2-x3)*(x2-x4)*(x3-x4) + d23*d24*d34*(x1-x3)*(x1-x4)*(x3-x4) + d12*d23*d34*(x1-x2)*(x1-x4)*(x2-x4)) / (2*(d12*d23 - d13*d24 + d14*d23 - d13*d14 - d12*d24 + d14*d22))

    return xc, yc, zc

