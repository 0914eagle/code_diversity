
import math

def get_center(points):
    point1, point2, point3, point4 = points
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    x3, y3, z3 = point3
    x4, y4, z4 = point4

    d1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    d2 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2 + (z3 - z1) ** 2)
    d3 = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2 + (z4 - z1) ** 2)
    d4 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2 + (z3 - z2) ** 2)
    d5 = math.sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2 + (z4 - z2) ** 2)
    d6 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2 + (z4 - z3) ** 2)

    denom = 2 * (d1 * d2 * d3 + d4 * d5 * d6)
    num1 = (d1 ** 2 + d2 ** 2 + d3 ** 2) * (d4 ** 2 + d5 ** 2 + d6 ** 2)
    num2 = (d1 ** 2 + d2 ** 2 + d3 ** 2) * (d5 ** 2 + d6 ** 2 + d4 ** 2)
    num3 = (d4 ** 2 + d5 ** 2 + d6 ** 2) * (d1 ** 2 + d2 ** 2 + d3 ** 2)

    xc = (num1 - num2 + num3) / denom
    yc = (num1 - num3 + num2) / denom
    zc = (num2 - num3 + num1) / denom

    return xc, yc, zc

